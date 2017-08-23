(function(angular) {

	'use strict';

	angular.module('snakeskin').controller('UserDetailController', function(userFactory, $routeParams, $scope) {
		$scope.activities = {
			'dataSources': {
				'display': 'Data Sources'
			},
			'recentActivities': {
				'display': 'Recent Activities'
			},
			'topActivities': {
				'display': 'Top Activities'
			},
			'totalActivities': {
				'display': 'Activity Counts by Month'
			},
		};

		$scope.showUserDataSources = function() {
			if ($scope.activities.dataSources.feed) {
				$scope.displayActivity = $scope.activities.dataSources;
				return;
			}

			userFactory.getUserDataSources($scope.tenant.id, $scope.user.id).success(function(dataSources) {
				$scope.activities.dataSources.feed = angular.toJson(dataSources, true);
				$scope.displayActivity = $scope.activities.dataSources;
			});
		};

		$scope.showUserRecentActivities = function() {
			if ($scope.activities.recentActivities.feed) {
				$scope.displayActivity = $scope.activities.recentActivities;
				return;
			}

			userFactory.getUserRecentActivities($scope.tenant.id, $scope.user.id).success(function(recentActivities) {
				$scope.activities.recentActivities.feed = angular.toJson(recentActivities, true);
				$scope.displayActivity = $scope.activities.recentActivities;
			});
		};

		$scope.showUserTopActivities = function() {
			if ($scope.activities.topActivities.feed) {
				$scope.displayActivity = $scope.activities.topActivities;
				return;
			}

			userFactory.getUserTopActivities($scope.tenant.id, $scope.user.id).success(function(topActivities) {
				$scope.activities.topActivities.feed = angular.toJson(topActivities, true);
				$scope.displayActivity = $scope.activities.topActivities;
			});
		};

		$scope.showUserTotalActivities = function() {
			if ($scope.activities.totalActivities.feed) {
				$scope.displayActivity = $scope.activities.totalActivities;
				return;
			}

			userFactory.getUserTotalActivities($scope.tenant.id, $scope.user.id).success(function(totalActivities) {
				$scope.activities.totalActivities.feed = angular.toJson(totalActivities, true);
				$scope.displayActivity = $scope.activities.totalActivities;
			});
		};

		var getUserProfile = function(tenantId, userId) {
			userFactory.getUserProfile(tenantId, userId).success(function(feed) {
				$scope.tenant = feed.tenant;
				$scope.user = feed.user;
			});
		};

		getUserProfile($routeParams.tenantId, $routeParams.userId);
	});

}(window.angular));
