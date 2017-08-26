(function(angular) {

	'use strict';

	angular.module('snakeskin').controller('TenantDetailController', function(tenantFactory, userFactory, $routeParams, $scope) {
		$scope.newUser = {
			externalId: '',
			canvasProfile: ''
		};

		var getTenant = function(tenantId) {
			tenantFactory.getTenantProfile(tenantId).success(function(tenant) {
				$scope.tenant = tenant;
			});
		};

		$scope.lookupCanvasUser = function() {
			userFactory.getUserCanvasProfile($scope.tenant.id, $scope.newUser.externalId).success(function(feed) {
				$scope.newUser.canvasProfile = feed;
			});
		};

		getTenant($routeParams.tenantId);
	});

}(window.angular));
