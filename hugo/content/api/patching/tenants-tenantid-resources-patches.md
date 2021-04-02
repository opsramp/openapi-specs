---
slug: tenants-tenantid-resources-patches
title: Get patches on a resource
description: >-
  Gets the details of installed, missing, or installation-failed patches for a
  client’s resources.


  ### Status Code

  NULL - The NULL value in the file indicates that the Agent did not trigger any
  installation job.


  0x0 - This value indicates that the patch is installed successfully.


  The following are error codes that identify installation failures when
  patching the device:


  |Code|

  |-----|

  | 0x80240020|

  | 0x80070643       |

  | 0x80070490       |

  | 0x800b0100       |

  | 0x80246007       |

  | 0x80070663       |

  | 0x80070652       |

  | 0x80246013       |

  | 0x80070005       |

  | 0x240006         |

  | 0x800f0831       |

  | 0x80092004       |

  | 0x8024000b       |

  | 0x80073701       |

  | 0x8024002d       |

  | 0x800f083f       |

  | 0x80070002       |

  | 0x80071a90       |

  | 0x8024200d       |

  | 0x8007371c       |

  | 0x800f082f       |

  | 0x80070308       |

  | 0x80070070       |

  | 0x80246012       |

  | 0x8000ffff       |

  | 0x8007006e       |

  | 0x80080005       |

  | 0x80240017       |

  | 0x800f0902       |

  | 0x80070020       |

  | 0x800700a1       |

  | 0x800705aa       |

  | 0x80004005       |

  | 0x800736b3       |

  | 0x80240009       |

  | 0x80070570       |

  | 0x80070570       |


  >##### Notes

  >There are special characters that can be used in a query string:

  >- (+) represents the next field and must be URL-encoded.

  >- (:) represents equals. An example is key : value.

  >- Space characters must be URL-encoded.


  ##### Query Variables

  |Query Variables|Values|Description|

  |-----|-----|------|

  |resourceUUID|NA|Unique ID of a resource.<br>Example:
  d5bce6fe-d19f-4ad7-8c50-5f639f2dd321. Use the Search Resources API to fetch
  the list of resources.|

  |startInstalledTime|yyyy-MM-ddTHH:mm: ssZ|Search for patches installed within
  a certain time frame. The startInstalledTime variable indicates the from
  time.<br>Example: 2018-10-10T09:20:00 0000|

  |endInstalledTime|yyyy-MM-ddTHH:mm: ssZ|The endInstalledTime variable
  indicates the to time.<br>Example:  2018-10-15T10:30:00 0000|

  |startScanTime|yyyy-MM-ddTHH:mm: ssZ|Starting time of searching the scan for
  patches.<br>The startScanTime variable indicates the from time.<br>Example:
  2018-10-10T09:20:00 0000|

  |endScanTime|yyyy-MM-ddTHH:mm: ssZ|End/Closing time of searching the scan for
  patches.<br>The endScanTime variable indicates the to time.<br>Example:
  2018-10-15T10:30:00 0000|

  |installedStatus|INPROGRESS, COMPLETED, FAILED, EXCLUDED,
  NEED_TO_INSTALL|Installed status of a patch.For example, to search for patches
  failed to install, provide installedStatus: FAILED.|

  |patchStatus|MISSING, INSTALLED|Search for missing patches or patches
  installed on the resources.|

  |category|CRITICAL, SECURITY|Category to which the patches belong.|

  |patchName|NA|Search for patches with the patch name.|

  |patchId|NA|Unique ID of a patch. To get the list of patches along with their
  unique Id, use the Search Patches API.<br>Example:
  PATCH-1fde1043-0d9c-4f3f-8a34-2d0afc3a137a.|

  |externalId|NA|External ID of a patch.|

  |severity|NA|Severity of a patch.|

  |approvalStatus|APPROVED, NOT_APPROVED|Approval status of a patch.For example,
  to search for approved patches, provide approvalStatus: APPROVED.|
tags:
  - patching
path: '/api/v2/tenants/{tenantId}/resources/patches'
request:
  - get
layout: api-doc
draft: false
---
