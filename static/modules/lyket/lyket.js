(function () {
	
	var lyket = angular.module('lyket', ['article']);
	
	lyket.config(['$interpolateProvider', function ($interpolateProvider) {
		
		$interpolateProvider.startSymbol('{{!').endSymbol('!}}');
		
	}]);
	
})();