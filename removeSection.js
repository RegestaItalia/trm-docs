(function () {
  var removeSection = function (hook, vm) {
    hook.beforeEach(function (markdown) {
      var lines = markdown.split('\n');
      var result = [];
      var skipSection = false;
      var sectionLevel = 0;

      for (var i = 0; i < lines.length; i++) {
        var line = lines[i];
        var match = line.match(/^(#{1,6})\s+/); // Match Markdown headers

        if (line.includes("<!-- {docsify-remove} -->")) {
          // Remove only this line and continue
          continue;
        }

        if (match) {
          var currentLevel = match[1].length; // Determine heading level

          if (skipSection && currentLevel > sectionLevel) {
            // If skipping, continue until we exit the section
            continue;
          }

          skipSection = false; // Reset
        }

        if (!skipSection) {
          result.push(line);
        }
      }

      return result.join('\n');
    });
  };

  $docsify = $docsify || {};
  $docsify.plugins = [].concat(removeSection, $docsify.plugins || []);
})();