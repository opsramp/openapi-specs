(function ($) {
    'use strict';

    // Headers' anchor link that shows on hover
    $(function () {
        // append anchor links to headings in markdown.
        var article = document.getElementsByTagName('main')[0];
        if (!article) {
            return;
        }
        var headings = article.querySelectorAll('h1, h2, h3, h4, h5, h6');
        headings.forEach(function (heading) {
            if (heading.id) {
                var toTop = document.createElement('a');
                // set visibility: hidden, not display: none to avoid layout change
                toTop.style.visibility = 'hidden';
                toTop.style.marginLeft = '0.6rem';
                toTop.style.opacity = '0.6';

                // [a11y] hide this from screen readers, etc..
                toTop.setAttribute('aria-hidden', 'true');

                // material insert_link icon in svg format
                toTop.innerHTML = ' <i class="fal fa-arrow-to-top fa-xs"></i>';
                toTop.href = '#';

                var a = document.createElement('a');
                // set visibility: hidden, not display: none to avoid layout change
                a.style.visibility = 'hidden';
                a.style.marginLeft = '0.6rem';
                a.style.opacity = '0.6';

                // [a11y] hide this from screen readers, etc..
                a.setAttribute('aria-hidden', 'true');

                // material insert_link icon in svg format
                a.innerHTML = ' <i class="fal fa-link fa-xs"></i>';
                a.href = '#' + heading.id;

                heading.insertAdjacentElement('beforeend', a);
                heading.insertAdjacentElement('beforeend', toTop);

                heading.addEventListener('mouseenter', function () {
                    toTop.style.visibility = 'initial';
                    a.style.visibility = 'initial';
                });
                heading.addEventListener('mouseleave', function () {
                    toTop.style.visibility = 'hidden';
                    a.style.visibility = 'hidden';
                });
            }

        });
    });

}(jQuery));
