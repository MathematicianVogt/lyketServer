(function () {
	
	var article = angular.module('article', ['overlay']);
	
	article.controller('article_controller', ['$scope', 'articles', function ($scope, articles) {
		
		$scope.article = {
			init: function () {
				
				$scope.$watch(function () { return articles.articles }, $scope.article.new_article);
				
			},
			new_article: function () {
				
				article = articles[$scope.n];
				
				if (!article) return; 
				
				$scope.headline = article.title;
				$scope.img = article.thumb;
				$scope.url = article.article_url;
				$scope.lykes = article.likes;
				$scope.dislykes = article.dislikes;
				
			},
			headline: "A Headline ryan is the greatest programmer in the world, Nobel Organization says",
			img: "http://i.imgur.com/yKpJaQr.png",
			url: "http://www.google.com",
			lykes: 1337,
			dislykes: 69,
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