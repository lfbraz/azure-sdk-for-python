# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource_py3 import Resource


class IoTSecuritySolutionAnalyticsModel(Resource):
    """Security Analytics of a security solution.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :ivar metrics: Security Analytics of a security solution
    :vartype metrics: ~azure.mgmt.security.models.IoTSeverityMetrics
    :ivar unhealthy_device_count: number of unhealthy devices
    :vartype unhealthy_device_count: int
    :ivar devices_metrics: The list of devices metrics by the aggregated date.
    :vartype devices_metrics:
     list[~azure.mgmt.security.models.IoTSecuritySolutionAnalyticsModelPropertiesDevicesMetricsItem]
    :param top_alerted_devices: The list of top 3 devices with the most
     attacked.
    :type top_alerted_devices:
     ~azure.mgmt.security.models.IoTSecurityAlertedDevicesList
    :param most_prevalent_device_alerts: The list of most prevalent 3 alerts.
    :type most_prevalent_device_alerts:
     ~azure.mgmt.security.models.IoTSecurityDeviceAlertsList
    :param most_prevalent_device_recommendations: The list of most prevalent 3
     recommendations.
    :type most_prevalent_device_recommendations:
     ~azure.mgmt.security.models.IoTSecurityDeviceRecommendationsList
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'metrics': {'readonly': True},
        'unhealthy_device_count': {'readonly': True},
        'devices_metrics': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'metrics': {'key': 'properties.metrics', 'type': 'IoTSeverityMetrics'},
        'unhealthy_device_count': {'key': 'properties.unhealthyDeviceCount', 'type': 'int'},
        'devices_metrics': {'key': 'properties.devicesMetrics', 'type': '[IoTSecuritySolutionAnalyticsModelPropertiesDevicesMetricsItem]'},
        'top_alerted_devices': {'key': 'properties.topAlertedDevices', 'type': 'IoTSecurityAlertedDevicesList'},
        'most_prevalent_device_alerts': {'key': 'properties.mostPrevalentDeviceAlerts', 'type': 'IoTSecurityDeviceAlertsList'},
        'most_prevalent_device_recommendations': {'key': 'properties.mostPrevalentDeviceRecommendations', 'type': 'IoTSecurityDeviceRecommendationsList'},
    }

    def __init__(self, *, top_alerted_devices=None, most_prevalent_device_alerts=None, most_prevalent_device_recommendations=None, **kwargs) -> None:
        super(IoTSecuritySolutionAnalyticsModel, self).__init__(**kwargs)
        self.metrics = None
        self.unhealthy_device_count = None
        self.devices_metrics = None
        self.top_alerted_devices = top_alerted_devices
        self.most_prevalent_device_alerts = most_prevalent_device_alerts
        self.most_prevalent_device_recommendations = most_prevalent_device_recommendations