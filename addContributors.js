(function () {
    var addContributors = function (hook, vm) {
        //add contributors as iframe in readme.md
        hook.beforeEach(function (markdown) {
            return markdown.replace(/<!-- {docsify-add CONTRIBUTORS} -->/g, "[Thanks goes to these wonderful people 🫂:](https://trmregistry.com/public/contributors?viewAll=true ':include :type=iframe width=\"100%\" height=\"550px\"')");
        });
    };

    $docsify = $docsify || {};
    $docsify.plugins = [].concat(addContributors, $docsify.plugins || []);
})();