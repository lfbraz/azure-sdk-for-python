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

from msrest.paging import Paged


class ApplicationGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationGateway <azure.mgmt.network.v2019_09_01.models.ApplicationGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationGatewayPaged, self).__init__(*args, **kwargs)
class ApplicationGatewaySslPredefinedPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationGatewaySslPredefinedPolicy <azure.mgmt.network.v2019_09_01.models.ApplicationGatewaySslPredefinedPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationGatewaySslPredefinedPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationGatewaySslPredefinedPolicyPaged, self).__init__(*args, **kwargs)
class ApplicationSecurityGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationSecurityGroup <azure.mgmt.network.v2019_09_01.models.ApplicationSecurityGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationSecurityGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationSecurityGroupPaged, self).__init__(*args, **kwargs)
class AvailableDelegationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AvailableDelegation <azure.mgmt.network.v2019_09_01.models.AvailableDelegation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AvailableDelegation]'}
    }

    def __init__(self, *args, **kwargs):

        super(AvailableDelegationPaged, self).__init__(*args, **kwargs)
class AvailableServiceAliasPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AvailableServiceAlias <azure.mgmt.network.v2019_09_01.models.AvailableServiceAlias>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AvailableServiceAlias]'}
    }

    def __init__(self, *args, **kwargs):

        super(AvailableServiceAliasPaged, self).__init__(*args, **kwargs)
class AzureFirewallPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AzureFirewall <azure.mgmt.network.v2019_09_01.models.AzureFirewall>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AzureFirewall]'}
    }

    def __init__(self, *args, **kwargs):

        super(AzureFirewallPaged, self).__init__(*args, **kwargs)
class AzureFirewallFqdnTagPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AzureFirewallFqdnTag <azure.mgmt.network.v2019_09_01.models.AzureFirewallFqdnTag>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AzureFirewallFqdnTag]'}
    }

    def __init__(self, *args, **kwargs):

        super(AzureFirewallFqdnTagPaged, self).__init__(*args, **kwargs)
class BastionHostPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BastionHost <azure.mgmt.network.v2019_09_01.models.BastionHost>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BastionHost]'}
    }

    def __init__(self, *args, **kwargs):

        super(BastionHostPaged, self).__init__(*args, **kwargs)
class DdosProtectionPlanPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DdosProtectionPlan <azure.mgmt.network.v2019_09_01.models.DdosProtectionPlan>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DdosProtectionPlan]'}
    }

    def __init__(self, *args, **kwargs):

        super(DdosProtectionPlanPaged, self).__init__(*args, **kwargs)
class EndpointServiceResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`EndpointServiceResult <azure.mgmt.network.v2019_09_01.models.EndpointServiceResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[EndpointServiceResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(EndpointServiceResultPaged, self).__init__(*args, **kwargs)
class ExpressRouteCircuitAuthorizationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCircuitAuthorization <azure.mgmt.network.v2019_09_01.models.ExpressRouteCircuitAuthorization>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCircuitAuthorization]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCircuitAuthorizationPaged, self).__init__(*args, **kwargs)
class ExpressRouteCircuitPeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCircuitPeering <azure.mgmt.network.v2019_09_01.models.ExpressRouteCircuitPeering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCircuitPeering]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCircuitPeeringPaged, self).__init__(*args, **kwargs)
class ExpressRouteCircuitConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCircuitConnection <azure.mgmt.network.v2019_09_01.models.ExpressRouteCircuitConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCircuitConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCircuitConnectionPaged, self).__init__(*args, **kwargs)
class PeerExpressRouteCircuitConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PeerExpressRouteCircuitConnection <azure.mgmt.network.v2019_09_01.models.PeerExpressRouteCircuitConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PeerExpressRouteCircuitConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PeerExpressRouteCircuitConnectionPaged, self).__init__(*args, **kwargs)
class ExpressRouteCircuitPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCircuit <azure.mgmt.network.v2019_09_01.models.ExpressRouteCircuit>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCircuit]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCircuitPaged, self).__init__(*args, **kwargs)
class ExpressRouteServiceProviderPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteServiceProvider <azure.mgmt.network.v2019_09_01.models.ExpressRouteServiceProvider>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteServiceProvider]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteServiceProviderPaged, self).__init__(*args, **kwargs)
class ExpressRouteCrossConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCrossConnection <azure.mgmt.network.v2019_09_01.models.ExpressRouteCrossConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCrossConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCrossConnectionPaged, self).__init__(*args, **kwargs)
class ExpressRouteCrossConnectionPeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteCrossConnectionPeering <azure.mgmt.network.v2019_09_01.models.ExpressRouteCrossConnectionPeering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteCrossConnectionPeering]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteCrossConnectionPeeringPaged, self).__init__(*args, **kwargs)
class ExpressRoutePortsLocationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRoutePortsLocation <azure.mgmt.network.v2019_09_01.models.ExpressRoutePortsLocation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRoutePortsLocation]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRoutePortsLocationPaged, self).__init__(*args, **kwargs)
class ExpressRoutePortPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRoutePort <azure.mgmt.network.v2019_09_01.models.ExpressRoutePort>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRoutePort]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRoutePortPaged, self).__init__(*args, **kwargs)
class ExpressRouteLinkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ExpressRouteLink <azure.mgmt.network.v2019_09_01.models.ExpressRouteLink>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ExpressRouteLink]'}
    }

    def __init__(self, *args, **kwargs):

        super(ExpressRouteLinkPaged, self).__init__(*args, **kwargs)
class FirewallPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`FirewallPolicy <azure.mgmt.network.v2019_09_01.models.FirewallPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FirewallPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(FirewallPolicyPaged, self).__init__(*args, **kwargs)
class FirewallPolicyRuleGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`FirewallPolicyRuleGroup <azure.mgmt.network.v2019_09_01.models.FirewallPolicyRuleGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FirewallPolicyRuleGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(FirewallPolicyRuleGroupPaged, self).__init__(*args, **kwargs)
class IpGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`IpGroup <azure.mgmt.network.v2019_09_01.models.IpGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[IpGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(IpGroupPaged, self).__init__(*args, **kwargs)
class LoadBalancerPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LoadBalancer <azure.mgmt.network.v2019_09_01.models.LoadBalancer>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LoadBalancer]'}
    }

    def __init__(self, *args, **kwargs):

        super(LoadBalancerPaged, self).__init__(*args, **kwargs)
class BackendAddressPoolPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BackendAddressPool <azure.mgmt.network.v2019_09_01.models.BackendAddressPool>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BackendAddressPool]'}
    }

    def __init__(self, *args, **kwargs):

        super(BackendAddressPoolPaged, self).__init__(*args, **kwargs)
class FrontendIPConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`FrontendIPConfiguration <azure.mgmt.network.v2019_09_01.models.FrontendIPConfiguration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FrontendIPConfiguration]'}
    }

    def __init__(self, *args, **kwargs):

        super(FrontendIPConfigurationPaged, self).__init__(*args, **kwargs)
class InboundNatRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`InboundNatRule <azure.mgmt.network.v2019_09_01.models.InboundNatRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[InboundNatRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(InboundNatRulePaged, self).__init__(*args, **kwargs)
class LoadBalancingRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`LoadBalancingRule <azure.mgmt.network.v2019_09_01.models.LoadBalancingRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LoadBalancingRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(LoadBalancingRulePaged, self).__init__(*args, **kwargs)
class OutboundRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`OutboundRule <azure.mgmt.network.v2019_09_01.models.OutboundRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[OutboundRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(OutboundRulePaged, self).__init__(*args, **kwargs)
class NetworkInterfacePaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkInterface <azure.mgmt.network.v2019_09_01.models.NetworkInterface>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkInterface]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkInterfacePaged, self).__init__(*args, **kwargs)
class ProbePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Probe <azure.mgmt.network.v2019_09_01.models.Probe>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Probe]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProbePaged, self).__init__(*args, **kwargs)
class NatGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NatGateway <azure.mgmt.network.v2019_09_01.models.NatGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NatGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(NatGatewayPaged, self).__init__(*args, **kwargs)
class NetworkInterfaceIPConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkInterfaceIPConfiguration <azure.mgmt.network.v2019_09_01.models.NetworkInterfaceIPConfiguration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkInterfaceIPConfiguration]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkInterfaceIPConfigurationPaged, self).__init__(*args, **kwargs)
class NetworkInterfaceTapConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkInterfaceTapConfiguration <azure.mgmt.network.v2019_09_01.models.NetworkInterfaceTapConfiguration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkInterfaceTapConfiguration]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkInterfaceTapConfigurationPaged, self).__init__(*args, **kwargs)
class NetworkProfilePaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkProfile <azure.mgmt.network.v2019_09_01.models.NetworkProfile>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkProfile]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkProfilePaged, self).__init__(*args, **kwargs)
class NetworkSecurityGroupPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkSecurityGroup <azure.mgmt.network.v2019_09_01.models.NetworkSecurityGroup>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkSecurityGroup]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkSecurityGroupPaged, self).__init__(*args, **kwargs)
class SecurityRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SecurityRule <azure.mgmt.network.v2019_09_01.models.SecurityRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SecurityRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(SecurityRulePaged, self).__init__(*args, **kwargs)
class NetworkWatcherPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NetworkWatcher <azure.mgmt.network.v2019_09_01.models.NetworkWatcher>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NetworkWatcher]'}
    }

    def __init__(self, *args, **kwargs):

        super(NetworkWatcherPaged, self).__init__(*args, **kwargs)
class PacketCaptureResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PacketCaptureResult <azure.mgmt.network.v2019_09_01.models.PacketCaptureResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PacketCaptureResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(PacketCaptureResultPaged, self).__init__(*args, **kwargs)
class ConnectionMonitorResultPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ConnectionMonitorResult <azure.mgmt.network.v2019_09_01.models.ConnectionMonitorResult>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ConnectionMonitorResult]'}
    }

    def __init__(self, *args, **kwargs):

        super(ConnectionMonitorResultPaged, self).__init__(*args, **kwargs)
class OperationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Operation <azure.mgmt.network.v2019_09_01.models.Operation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Operation]'}
    }

    def __init__(self, *args, **kwargs):

        super(OperationPaged, self).__init__(*args, **kwargs)
class PrivateEndpointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpoint <azure.mgmt.network.v2019_09_01.models.PrivateEndpoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointPaged, self).__init__(*args, **kwargs)
class AvailablePrivateEndpointTypePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AvailablePrivateEndpointType <azure.mgmt.network.v2019_09_01.models.AvailablePrivateEndpointType>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AvailablePrivateEndpointType]'}
    }

    def __init__(self, *args, **kwargs):

        super(AvailablePrivateEndpointTypePaged, self).__init__(*args, **kwargs)
class PrivateLinkServicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateLinkService <azure.mgmt.network.v2019_09_01.models.PrivateLinkService>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateLinkService]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateLinkServicePaged, self).__init__(*args, **kwargs)
class PrivateEndpointConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PrivateEndpointConnection <azure.mgmt.network.v2019_09_01.models.PrivateEndpointConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PrivateEndpointConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(PrivateEndpointConnectionPaged, self).__init__(*args, **kwargs)
class AutoApprovedPrivateLinkServicePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AutoApprovedPrivateLinkService <azure.mgmt.network.v2019_09_01.models.AutoApprovedPrivateLinkService>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AutoApprovedPrivateLinkService]'}
    }

    def __init__(self, *args, **kwargs):

        super(AutoApprovedPrivateLinkServicePaged, self).__init__(*args, **kwargs)
class PublicIPAddressPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PublicIPAddress <azure.mgmt.network.v2019_09_01.models.PublicIPAddress>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PublicIPAddress]'}
    }

    def __init__(self, *args, **kwargs):

        super(PublicIPAddressPaged, self).__init__(*args, **kwargs)
class PublicIPPrefixPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PublicIPPrefix <azure.mgmt.network.v2019_09_01.models.PublicIPPrefix>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PublicIPPrefix]'}
    }

    def __init__(self, *args, **kwargs):

        super(PublicIPPrefixPaged, self).__init__(*args, **kwargs)
class RouteFilterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`RouteFilter <azure.mgmt.network.v2019_09_01.models.RouteFilter>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RouteFilter]'}
    }

    def __init__(self, *args, **kwargs):

        super(RouteFilterPaged, self).__init__(*args, **kwargs)
class RouteFilterRulePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RouteFilterRule <azure.mgmt.network.v2019_09_01.models.RouteFilterRule>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RouteFilterRule]'}
    }

    def __init__(self, *args, **kwargs):

        super(RouteFilterRulePaged, self).__init__(*args, **kwargs)
class RouteTablePaged(Paged):
    """
    A paging container for iterating over a list of :class:`RouteTable <azure.mgmt.network.v2019_09_01.models.RouteTable>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[RouteTable]'}
    }

    def __init__(self, *args, **kwargs):

        super(RouteTablePaged, self).__init__(*args, **kwargs)
class RoutePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Route <azure.mgmt.network.v2019_09_01.models.Route>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Route]'}
    }

    def __init__(self, *args, **kwargs):

        super(RoutePaged, self).__init__(*args, **kwargs)
class BgpServiceCommunityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BgpServiceCommunity <azure.mgmt.network.v2019_09_01.models.BgpServiceCommunity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BgpServiceCommunity]'}
    }

    def __init__(self, *args, **kwargs):

        super(BgpServiceCommunityPaged, self).__init__(*args, **kwargs)
class ServiceEndpointPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServiceEndpointPolicy <azure.mgmt.network.v2019_09_01.models.ServiceEndpointPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServiceEndpointPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServiceEndpointPolicyPaged, self).__init__(*args, **kwargs)
class ServiceEndpointPolicyDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ServiceEndpointPolicyDefinition <azure.mgmt.network.v2019_09_01.models.ServiceEndpointPolicyDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ServiceEndpointPolicyDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(ServiceEndpointPolicyDefinitionPaged, self).__init__(*args, **kwargs)
class UsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Usage <azure.mgmt.network.v2019_09_01.models.Usage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Usage]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsagePaged, self).__init__(*args, **kwargs)
class VirtualNetworkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetwork <azure.mgmt.network.v2019_09_01.models.VirtualNetwork>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetwork]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkPaged, self).__init__(*args, **kwargs)
class VirtualNetworkUsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkUsage <azure.mgmt.network.v2019_09_01.models.VirtualNetworkUsage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkUsage]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkUsagePaged, self).__init__(*args, **kwargs)
class SubnetPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Subnet <azure.mgmt.network.v2019_09_01.models.Subnet>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Subnet]'}
    }

    def __init__(self, *args, **kwargs):

        super(SubnetPaged, self).__init__(*args, **kwargs)
class VirtualNetworkPeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkPeering <azure.mgmt.network.v2019_09_01.models.VirtualNetworkPeering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkPeering]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkPeeringPaged, self).__init__(*args, **kwargs)
class VirtualNetworkGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkGateway <azure.mgmt.network.v2019_09_01.models.VirtualNetworkGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkGatewayPaged, self).__init__(*args, **kwargs)
class VirtualNetworkGatewayConnectionListEntityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkGatewayConnectionListEntity <azure.mgmt.network.v2019_09_01.models.VirtualNetworkGatewayConnectionListEntity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkGatewayConnectionListEntity]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkGatewayConnectionListEntityPaged, self).__init__(*args, **kwargs)
class VirtualNetworkGatewayConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkGatewayConnection <azure.mgmt.network.v2019_09_01.models.VirtualNetworkGatewayConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkGatewayConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkGatewayConnectionPaged, self).__init__(*args, **kwargs)
class LocalNetworkGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`LocalNetworkGateway <azure.mgmt.network.v2019_09_01.models.LocalNetworkGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[LocalNetworkGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(LocalNetworkGatewayPaged, self).__init__(*args, **kwargs)
class VirtualNetworkTapPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualNetworkTap <azure.mgmt.network.v2019_09_01.models.VirtualNetworkTap>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualNetworkTap]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualNetworkTapPaged, self).__init__(*args, **kwargs)
class VirtualRouterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualRouter <azure.mgmt.network.v2019_09_01.models.VirtualRouter>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualRouter]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualRouterPaged, self).__init__(*args, **kwargs)
class VirtualRouterPeeringPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualRouterPeering <azure.mgmt.network.v2019_09_01.models.VirtualRouterPeering>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualRouterPeering]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualRouterPeeringPaged, self).__init__(*args, **kwargs)
class VirtualWANPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualWAN <azure.mgmt.network.v2019_09_01.models.VirtualWAN>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualWAN]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualWANPaged, self).__init__(*args, **kwargs)
class VpnSitePaged(Paged):
    """
    A paging container for iterating over a list of :class:`VpnSite <azure.mgmt.network.v2019_09_01.models.VpnSite>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VpnSite]'}
    }

    def __init__(self, *args, **kwargs):

        super(VpnSitePaged, self).__init__(*args, **kwargs)
class VpnSiteLinkPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VpnSiteLink <azure.mgmt.network.v2019_09_01.models.VpnSiteLink>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VpnSiteLink]'}
    }

    def __init__(self, *args, **kwargs):

        super(VpnSiteLinkPaged, self).__init__(*args, **kwargs)
class VpnServerConfigurationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VpnServerConfiguration <azure.mgmt.network.v2019_09_01.models.VpnServerConfiguration>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VpnServerConfiguration]'}
    }

    def __init__(self, *args, **kwargs):

        super(VpnServerConfigurationPaged, self).__init__(*args, **kwargs)
class VirtualHubPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualHub <azure.mgmt.network.v2019_09_01.models.VirtualHub>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualHub]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualHubPaged, self).__init__(*args, **kwargs)
class HubVirtualNetworkConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`HubVirtualNetworkConnection <azure.mgmt.network.v2019_09_01.models.HubVirtualNetworkConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[HubVirtualNetworkConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(HubVirtualNetworkConnectionPaged, self).__init__(*args, **kwargs)
class VpnGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VpnGateway <azure.mgmt.network.v2019_09_01.models.VpnGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VpnGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(VpnGatewayPaged, self).__init__(*args, **kwargs)
class VpnConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VpnConnection <azure.mgmt.network.v2019_09_01.models.VpnConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VpnConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(VpnConnectionPaged, self).__init__(*args, **kwargs)
class VpnSiteLinkConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`VpnSiteLinkConnection <azure.mgmt.network.v2019_09_01.models.VpnSiteLinkConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VpnSiteLinkConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(VpnSiteLinkConnectionPaged, self).__init__(*args, **kwargs)
class P2SVpnGatewayPaged(Paged):
    """
    A paging container for iterating over a list of :class:`P2SVpnGateway <azure.mgmt.network.v2019_09_01.models.P2SVpnGateway>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[P2SVpnGateway]'}
    }

    def __init__(self, *args, **kwargs):

        super(P2SVpnGatewayPaged, self).__init__(*args, **kwargs)
class VirtualHubRouteTableV2Paged(Paged):
    """
    A paging container for iterating over a list of :class:`VirtualHubRouteTableV2 <azure.mgmt.network.v2019_09_01.models.VirtualHubRouteTableV2>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[VirtualHubRouteTableV2]'}
    }

    def __init__(self, *args, **kwargs):

        super(VirtualHubRouteTableV2Paged, self).__init__(*args, **kwargs)
class WebApplicationFirewallPolicyPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WebApplicationFirewallPolicy <azure.mgmt.network.v2019_09_01.models.WebApplicationFirewallPolicy>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WebApplicationFirewallPolicy]'}
    }

    def __init__(self, *args, **kwargs):

        super(WebApplicationFirewallPolicyPaged, self).__init__(*args, **kwargs)
