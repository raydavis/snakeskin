(function(angular) {

	'use strict';

	angular.module('snakeskin').factory('tenantFactory', function($http) {
		var getTenantList = function() {
	    return $http.get('/api/tenant');
		};

		var getTenantProfile = function(tenantId) {
	    return $http.get('/api/tenant/' + tenantId);
		};

		return {
			'getTenantList': getTenantList,
	  	'getTenantProfile': getTenantProfile
		}
	});

}(window.angular));
