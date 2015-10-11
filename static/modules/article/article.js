(function () {
	
	var article = angular.module('article', ['overlay']);
	
	article.controller('article_controller', ['$scope', function ($scope) {
		
		$scope.article = {
			init: function () {},
			headline: "A Headline ryan is the greatest programmer in the world, Nobel Organization says",
			img: "http://i.imgur.com/yKpJaQr.png",
			url: "http://www.google.com",
			lyke: function () {
				console.log('Lyked!');
			},
			dislyke: function () {
				console.log('Dislyked');
			},
			overlay: {
				display: false,
				mouseover : function () {
					$scope.article.overlay.display = true;
				},
				mouseout: function () {
					$scope.article.overlay.display = false;
				}
			}
		}
		
		$scope.article.init();
		
	}]);
	
	article.directive('lykArticle', [function () {
		
		return {
			restrict: 'E',
			templateUrl: '/static/modules/article/article.html',
			controller: 'article_controller',
			scope: {
				n: '='
			}
		};
		
	}]);
	
})();