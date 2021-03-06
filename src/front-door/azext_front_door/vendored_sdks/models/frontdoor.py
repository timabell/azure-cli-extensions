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

from .resource import Resource


class Frontdoor(Resource):
    """Frontdoor represents a collection of backend endpoints to route traffic to
    along with rules that specify how traffic is sent there.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param id: Resource ID.
    :type id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location.
    :type location: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param friendly_name: A friendly name for the frontdoor
    :type friendly_name: str
    :param routing_rules: Routing rules associated with this Frontdoor.
    :type routing_rules: list[~azure.mgmt.frontdoor.models.RoutingRule]
    :param load_balancing_settings: Load balancing settings associated with
     this Frontdoor instance.
    :type load_balancing_settings:
     list[~azure.mgmt.frontdoor.models.LoadBalancingSettingsModel]
    :param health_probe_settings: Health probe settings associated with this
     Frontdoor instance.
    :type health_probe_settings:
     list[~azure.mgmt.frontdoor.models.HealthProbeSettingsModel]
    :param backend_pools: Backend pools available to routing rules.
    :type backend_pools: list[~azure.mgmt.frontdoor.models.BackendPool]
    :param frontend_endpoints: Frontend endpoints available to routing rules.
    :type frontend_endpoints:
     list[~azure.mgmt.frontdoor.models.FrontendEndpoint]
    :param enabled_state: Operational status of the Frontdoor load balancer.
     Permitted values are 'Enabled' or 'Disabled'. Possible values include:
     'Enabled', 'Disabled'
    :type enabled_state: str or
     ~azure.mgmt.frontdoor.models.FrontdoorEnabledState
    :param resource_state: Resource status of the Frontdoor. Possible values
     include: 'Creating', 'Enabling', 'Enabled', 'Disabling', 'Disabled',
     'Deleting'
    :type resource_state: str or
     ~azure.mgmt.frontdoor.models.FrontdoorResourceState
    :ivar provisioning_state: Provisioning state of the Frontdoor.
    :vartype provisioning_state: str
    :ivar cname: The host that each frontendEndpoint must CNAME to.
    :vartype cname: str
    """

    _validation = {
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'cname': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'friendly_name': {'key': 'properties.friendlyName', 'type': 'str'},
        'routing_rules': {'key': 'properties.routingRules', 'type': '[RoutingRule]'},
        'load_balancing_settings': {'key': 'properties.loadBalancingSettings', 'type': '[LoadBalancingSettingsModel]'},
        'health_probe_settings': {'key': 'properties.healthProbeSettings', 'type': '[HealthProbeSettingsModel]'},
        'backend_pools': {'key': 'properties.backendPools', 'type': '[BackendPool]'},
        'frontend_endpoints': {'key': 'properties.frontendEndpoints', 'type': '[FrontendEndpoint]'},
        'enabled_state': {'key': 'properties.enabledState', 'type': 'str'},
        'resource_state': {'key': 'properties.resourceState', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'cname': {'key': 'properties.cname', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Frontdoor, self).__init__(**kwargs)
        self.friendly_name = kwargs.get('friendly_name', None)
        self.routing_rules = kwargs.get('routing_rules', None)
        self.load_balancing_settings = kwargs.get('load_balancing_settings', None)
        self.health_probe_settings = kwargs.get('health_probe_settings', None)
        self.backend_pools = kwargs.get('backend_pools', None)
        self.frontend_endpoints = kwargs.get('frontend_endpoints', None)
        self.enabled_state = kwargs.get('enabled_state', None)
        self.resource_state = kwargs.get('resource_state', None)
        self.provisioning_state = None
        self.cname = None
