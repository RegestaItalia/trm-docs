(function () {
  var fixRoute = function (hook, vm) {

    // Invoked on each page load after new markdown has been transformed to HTML.
    // Supports asynchronous tasks (see afterEach documentation for details).
    hook.doneEach(function () {
      var aLi = $(".sidebar-nav").find("li");
	  for(var i = 0; i < aLi.length; i++){
		  var li = $(aLi[i]);
		  var aA = li.find("a");
		  for(var k = 0; k < aA.length; k++){
			  var a = aA[k];
			  if(a.href){
				  a.href = a.href.replace("/docs/docs/", "/docs/");
			  }
		  }
	  }
    });
  };

  // Add plugin to docsify's plugin array
  $docsify = $docsify || {};
  $docsify.plugins = [].concat(fixRoute, $docsify.plugins || []);
})();