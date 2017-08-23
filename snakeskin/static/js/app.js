(function(angular) {

  angular.module('snakeskin', ['ngRoute']);

  var bootstrap = function() {
    angular.element(document).ready(function() {
      angular.bootstrap(document, [ 'snakeskin' ]);
    });
  };

  bootstrap();

}(window.angular));
