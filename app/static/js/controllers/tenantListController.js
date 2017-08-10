(function(angular) {

	'use strict';

	angular.module('snakeskin').controller('TenantListController', function(tenantFactory, $scope) {
		var getTenants = function() {
			tenantFactory.getTenantList().success(function(tenants) {
				$scope.tenants = tenants;
			});
		};

		getTenants();
	});

}(window.angular));
