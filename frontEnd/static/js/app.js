'use strict';

var myApp = angular.module('myApp', [
    'ngRoute',
    'ngResource'
]);

myApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/', {
			    templateUrl: '../static/partials/main.html',
			    controller: "MainController"
			}).
		otherwise({
		    redirectTo: '/'
		});
	}]);