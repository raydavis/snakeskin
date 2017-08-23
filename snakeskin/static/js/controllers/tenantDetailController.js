(function(angular) {

	'use strict';

	angular.module('snakeskin').controller('TenantDetailController', function(tenantFactory, $routeParams, $scope) {
		var getTenant = function(tenantId) {
			tenantFactory.getTenantProfile(tenantId).success(function(tenant) {
				$scope.tenant = tenant;
			});
		};

		getTenant($routeParams.tenantId);
	});

}(window.angular));
