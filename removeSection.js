(function () {
  var removeSection = function (hook, vm) {
    hook.beforeEach(function (markdown) {
		// Define a regular expression to match sections to be removed
		var regex = /(^|\n)(#{1,6}.*?)(<!-- {docsify-remove} -->\n([\s\S]*?)(?=(\n#{1,6}|$)))/g;

		// Replace matched sections with an empty string
		var cleanedMarkdown = markdown.replace(regex, '');

		return cleanedMarkdown;
    });
  };

  $docsify = $docsify || {};
  $docsify.plugins = [].concat(removeSection, $docsify.plugins || []);
})();