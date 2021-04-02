#!/usr/bin/env node

const { argv } = require('yargs')
  .scriptName('api-build')
  .options('d', {
    alias: 'data',
    describe: 'This is the directory where the data files are generated.',
    default: 'data/api/',
    type: 'string',
  })
  .options('c', {
    alias: 'content',
    describe: 'This is the directory where the content files are generated.',
    default: 'content/api/',
    type: 'string',
  })
  .options('i', {
    alias: 'internal',
    describe: 'Build all endpoints marked "internal"',
    type: 'boolean',
  })

const SwaggerParser = require('@apidevtools/swagger-parser')
const slugify = require('slugify')
const yaml = require('js-yaml')

const fs = require('fs')
const path = require('path')

// To the moon!
Main()

/**
 * Main() - Clones the API spec to a temporary location, then runs all of our helpers in sequence.
 */
function Main() {
  const ignoreTags = argv.i ? [] : ['internal']

  yamls = initializeBuild()

  // Loop through each yaml that was returned
  yamls.forEach(async (cur) => {
    const pathToYAML = path.join('../v2', cur.file)

    const api = await SwaggerParser.validate(pathToYAML)
    const paths = Object.entries(api.paths)

    prepLocation(cur.tag, argv.c)
    prepLocation(cur.tag, argv.d)

    generateContent(cur.tag, paths, ignoreTags)
    generateData(cur.tag, paths, ignoreTags)
  })
}

/**
 * initializeBuild() - Returns a promise which will contain a list of our API YAMLs when fulfilled.
 */
function initializeBuild() {
  const regex = /opsramp-([\w-]+?).v2.yaml/g
  const tmpDir = '../v2'

  try {
    fs.accessSync(tmpDir, fs.F_OK)

    // Get a list of the files we find in the api /v2/ directory
    // Then filter them to only include those we want
    let files = fs.readdirSync(tmpDir)
    files = files.filter((val) => val.match(regex))

    // Create an array of objects containing the file name and its associated tag
    return files.map((val) => {
      const matches = [...val.matchAll(regex)]
      return {
        file: matches[0][0],
        tag: matches[0][1],
      }
    })
  } catch {
    console.error(`The path ${tmpDir} could not be accessed.`)
  }
}

/**
 * prepLocation() - Forming a fully qualified path from the tag and directory supplied
 * from the command line, prep our file location. Files must be removed prior to
 * generating new files, so that non-existent endpoints are not left orphaned.
 */
function prepLocation(tag, dir) {
  let location = path.join(__dirname, dir, tag)

  // Check if our directory exists, if not, create it
  if (!fs.existsSync(location)) {
    fs.mkdirSync(location, { recursive: true })
  } else {
    // If it exists, glob for files and prep
    let locationContents = fs.readdirSync(location)

    locationContents.forEach((file) => {
      const pathToFile = path.join(location, file)

      // Only remove the file if it's not an _index.md
      // This is an array in case we need to ignore other files later
      if (!['_index.md'].includes(file)) {
        fs.unlinkSync(pathToFile)
      }
    })
  }
}

/**
 * generateContent() - Creates all of the markdown files needed by Hugo
 */
function generateContent(tag, endpoints, ignore) {
  for (const [endpoint, data] of endpoints) {
    const slug = getSlugForEndpoint(endpoint)
    const requestMethods = getRequestMethods(data)

    if (ignore.length) {
      const foundIgnore = requestMethods.filter((method) => {
        const found = data[method].tags.some((tag) => ignore.includes(tag))
        return found
      })
      if (requestMethods.length === foundIgnore.length) {
        continue
      }
    }

    // Build the frontmatter object
    const frontmatter = {
      slug: slug,
      title: data.summary,
      description: data.description,
      tags: [tag],
      path: endpoint,
      request: requestMethods.sort(),
      layout: 'api-doc',
      draft: false,
    }

    const fileContents = `---\n${yaml.dump(frontmatter)}---\n`
    const fileLocation = path.join(__dirname, argv.c, tag, slug + '.md')

    // Fire these off asynchronously so the rest of the app can continue
    fs.writeFile(fileLocation, fileContents, (err) => {
      if (err) {
        console.error(err)
      }
    })
  }
}

/**
 * generateData() - Creates all of the data files needed by Hugo
 */
function generateData(tag, paths, ignore) {
  for (const [endpoint, data] of paths) {
    const slug = getSlugForEndpoint(endpoint)
    const requestMethods = getRequestMethods(data)

    const operations = requestMethods
      .filter((method) => {
        const tags = data[method].tags
        return !tags.some((tag) => ignore.includes(tag))
      })
      .map((method) => {
        const methodData = data[method]

        const newOperation = {
          description: methodData.description ?? '',
          parameters: methodData.parameters ?? '',
        }

        if ('requestBody' in methodData) {
          const requestBody = {
            content: 'application/json',
            schema: methodData.requestBody.content['application/json'].schema,
          }

          const examples =
            methodData.requestBody.content['application/json'].examples

          newOperation.requestBody = requestBody
          newOperation.requestBodyExamples = examples
        }

        if ('responses' in methodData) {
          const responses = {}

          for (const [key, value] of Object.entries(methodData.responses)) {
            responses[key] = {
              description: value.description || '',
            }

            if ('content' in value) {
              const content = value.content['application/json']

              if (undefined == content) {
                // @TODO Needs better error handling
                console.err('Undefined found in: ' + slug)
              } else {
                if ('schema' in content) {
                  responses[key].schema =
                    value.content['application/json'].schema
                }
                if ('examples' in content) {
                  responses[key].examples =
                    value.content['application/json'].examples
                }
              }
            }
          }
          newOperation.responses = responses
        }

        return [method, newOperation]
      })

    // All operations were ignored, skip this iteration
    if (operations.length === 0) {
      continue
    }

    let newObject = {
      summary: data.summary,
      description: data.description,
      operations: Object.fromEntries(operations),
      parameters: data.parameters,
    }

    const fileContents = JSON.stringify(newObject)
    const fileLocation = path.join(__dirname, argv.d, tag, slug + '.json')

    fs.writeFile(fileLocation, fileContents, (err) => {
      if (err) {
        console.error(err)
      }
    })
  }
}

function getSlugForEndpoint(endpoint) {
  // Slugify just removes these, so we need spaces
  let slug = endpoint.replace(/[\/{}]/gu, ' ')
  slug = slugify(slug, {
    lower: true,
  })

  if (slug.indexOf('api-v2-') !== -1) {
    slug = slug.substring(7)
  }

  return slug
}

function getRequestMethods(data) {
  const allowedMethods = ['post', 'get', 'put', 'patch', 'delete']
  const requestMethods = Object.keys(data)

  return requestMethods.filter((val) => allowedMethods.includes(val))
}
