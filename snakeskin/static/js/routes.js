(function(angular) {

	'use strict';

	angular.module('snakeskin').config(function($locationProvider, $routeProvider) {
		$routeProvider
			.when('/', {
				templateUrl: 'static/templates/tenantList.html',
				controller: 'TenantListController'
			})
			.when('/tenant/:tenantId', {
				templateUrl: 'static/templates/tenantDetail.html',
				controller: 'TenantDetailController'
			})
			.when('/tenant/:tenantId/user/:userId', {
				templateUrl: 'static/templates/userDetail.html',
				controller: 'UserDetailController'
			})
			.otherwise({
				redirectTo: '/'
			});

		$locationProvider.html5Mode(true);
	});

}(window.angular));
