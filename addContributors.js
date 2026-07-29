(function () {
    var contributorsUrl = "https://trmregistry.com/public/contributors";
    var contributorsStylesId = "contributors-embed-styles";

    var addContributors = function (hook, vm) {
        hook.mounted(function () {
            if (document.getElementById(contributorsStylesId)) {
                return;
            }

            var styles = document.createElement("style");
            styles.id = contributorsStylesId;
            styles.textContent = [
                ".contributors-embed {",
                "    width: 100%;",
                "    max-width: 100%;",
                "    overflow: hidden;",
                "}",
                ".contributors-embed__image-link {",
                "    display: none;",
                "}",
                ".contributors-embed__iframe {",
                "    display: block;",
                "    width: 100%;",
                "    max-width: 100%;",
                "    height: 800px;",
                "    border: 0;",
                "    overflow: hidden;",
                "}",
                "@media screen and (max-width: 600px) {",
                "    .contributors-embed__iframe {",
                "        display: none;",
                "    }",
                "    .contributors-embed__image-link {",
                "        display: block;",
                "        width: 100%;",
                "        max-width: 100%;",
                "        overflow: hidden;",
                "    }",
                "    .contributors-embed__image {",
                "        display: block;",
                "        width: 100%;",
                "        max-width: 100%;",
                "        height: auto;",
                "        object-fit: contain;",
                "    }",
                "}"
            ].join("\n");

            document.head.appendChild(styles);
        });

        hook.beforeEach(function (markdown) {
            var contributors = [
                '<div class="contributors-embed">',
                '    <a class="contributors-embed__image-link" href="' + contributorsUrl + '" target="_blank" rel="noopener" aria-label="View TRM contributors">',
                '        <img class="contributors-embed__image" src="' + contributorsUrl + '?image=true" alt="TRM project contributors" loading="lazy">',
                "    </a>",
                '    <iframe class="contributors-embed__iframe" src="' + contributorsUrl + '" title="TRM project contributors" loading="lazy" scrolling="no"></iframe>',
                "</div>"
            ].join("\n");

            return markdown.replace(/<!-- {docsify-add CONTRIBUTORS} -->/g, contributors);
        });
    };

    $docsify = $docsify || {};
    $docsify.plugins = [].concat(addContributors, $docsify.plugins || []);
})();
