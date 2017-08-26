(function(angular) {

	'use strict';

	angular.module('snakeskin').factory('userFactory', function($http) {
		var getUserCanvasProfile = function(tenantId, userId) {
	    return $http.get('/api/tenant/' + tenantId + '/user/' + userId + '/canvas_profile');
		};

		var getUserDataSources = function(tenantId, userId) {
	    return $http.get('/api/tenant/' + tenantId + '/user/' + userId + '/data_sources');
		};

		var getUserProfile = function(tenantId, userId) {
	    return $http.get('/api/tenant/' + tenantId + '/user/' + userId);
		};

		var getUserRecentActivities = function(tenantId, userId) {
	    return $http.get('/api/tenant/' + tenantId + '/user/' + userId + '/recent_activities');
		};

		var getUserTopActivities = function(tenantId, userId) {
	    return $http.get('/api/tenant/' + tenantId + '/user/' + userId + '/top_activities');
		};

		var getUserTotalActivities = function(tenantId, userId) {
	    return $http.get('/api/tenant/' + tenantId + '/user/' + userId + '/total_activities');
		};

	  return {
	  	'getUserCanvasProfile': getUserCanvasProfile,
	  	'getUserDataSources': getUserDataSources,
	    'getUserProfile': getUserProfile,
	  	'getUserRecentActivities': getUserRecentActivities,
	  	'getUserTopActivities': getUserTopActivities,
	  	'getUserTotalActivities': getUserTotalActivities
	  };
	});

}(window.angular));
