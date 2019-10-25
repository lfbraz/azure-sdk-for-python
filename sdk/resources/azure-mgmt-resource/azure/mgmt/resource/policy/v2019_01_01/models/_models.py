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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorResponse(Model):
    """Error response indicates Azure Resource Manager is not able to process the
    incoming request. The reason is provided in the error message.

    :param http_status: Http status code.
    :type http_status: str
    :param error_code: Error code.
    :type error_code: str
    :param error_message: Error message indicating why the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'http_status': {'key': 'httpStatus', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.http_status = kwargs.get('http_status', None)
        self.error_code = kwargs.get('error_code', None)
        self.error_message = kwargs.get('error_message', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Identity(Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal ID of the resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of the resource identity.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: 'SystemAssigned',
     'None'
    :type type: str or
     ~azure.mgmt.resource.policy.v2019_01_01.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ResourceIdentityType'},
    }

    def __init__(self, **kwargs):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class PolicyAssignment(Model):
    """The policy assignment.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param display_name: The display name of the policy assignment.
    :type display_name: str
    :param policy_definition_id: The ID of the policy definition or policy set
     definition being assigned.
    :type policy_definition_id: str
    :param scope: The scope for the policy assignment.
    :type scope: str
    :param not_scopes: The policy's excluded scopes.
    :type not_scopes: list[str]
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    :param description: This message will be part of response in case of
     policy violation.
    :type description: str
    :param metadata: The policy assignment metadata.
    :type metadata: object
    :ivar id: The ID of the policy assignment.
    :vartype id: str
    :ivar type: The type of the policy assignment.
    :vartype type: str
    :ivar name: The name of the policy assignment.
    :vartype name: str
    :param sku: The policy sku. This property is optional, obsolete, and will
     be ignored.
    :type sku: ~azure.mgmt.resource.policy.v2019_01_01.models.PolicySku
    :param location: The location of the policy assignment. Only required when
     utilizing managed identity.
    :type location: str
    :param identity: The managed identity associated with the policy
     assignment.
    :type identity: ~azure.mgmt.resource.policy.v2019_01_01.models.Identity
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
    }

    _attribute_map = {
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'policy_definition_id': {'key': 'properties.policyDefinitionId', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'not_scopes': {'key': 'properties.notScopes', 'type': '[str]'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'PolicySku'},
        'location': {'key': 'location', 'type': 'str'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(self, **kwargs):
        super(PolicyAssignment, self).__init__(**kwargs)
        self.display_name = kwargs.get('display_name', None)
        self.policy_definition_id = kwargs.get('policy_definition_id', None)
        self.scope = kwargs.get('scope', None)
        self.not_scopes = kwargs.get('not_scopes', None)
        self.parameters = kwargs.get('parameters', None)
        self.description = kwargs.get('description', None)
        self.metadata = kwargs.get('metadata', None)
        self.id = None
        self.type = None
        self.name = None
        self.sku = kwargs.get('sku', None)
        self.location = kwargs.get('location', None)
        self.identity = kwargs.get('identity', None)


class PolicyDefinition(Model):
    """The policy definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param policy_type: The type of policy definition. Possible values are
     NotSpecified, BuiltIn, and Custom. Possible values include:
     'NotSpecified', 'BuiltIn', 'Custom'
    :type policy_type: str or
     ~azure.mgmt.resource.policy.v2019_01_01.models.PolicyType
    :param mode: The policy definition mode. Some examples are All, Indexed,
     Microsoft.KeyVault.Data.
    :type mode: str
    :param display_name: The display name of the policy definition.
    :type display_name: str
    :param description: The policy definition description.
    :type description: str
    :param policy_rule: The policy rule.
    :type policy_rule: object
    :param metadata: The policy definition metadata.
    :type metadata: object
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    :ivar id: The ID of the policy definition.
    :vartype id: str
    :ivar name: The name of the policy definition.
    :vartype name: str
    :ivar type: The type of the resource
     (Microsoft.Authorization/policyDefinitions).
    :vartype type: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'policy_rule': {'key': 'properties.policyRule', 'type': 'object'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicyDefinition, self).__init__(**kwargs)
        self.policy_type = kwargs.get('policy_type', None)
        self.mode = kwargs.get('mode', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.policy_rule = kwargs.get('policy_rule', None)
        self.metadata = kwargs.get('metadata', None)
        self.parameters = kwargs.get('parameters', None)
        self.id = None
        self.name = None
        self.type = None


class PolicyDefinitionReference(Model):
    """The policy definition reference.

    :param policy_definition_id: The ID of the policy definition or policy set
     definition.
    :type policy_definition_id: str
    :param parameters: Required if a parameter is used in policy rule.
    :type parameters: object
    """

    _attribute_map = {
        'policy_definition_id': {'key': 'policyDefinitionId', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(PolicyDefinitionReference, self).__init__(**kwargs)
        self.policy_definition_id = kwargs.get('policy_definition_id', None)
        self.parameters = kwargs.get('parameters', None)


class PolicySetDefinition(Model):
    """The policy set definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param policy_type: The type of policy definition. Possible values are
     NotSpecified, BuiltIn, and Custom. Possible values include:
     'NotSpecified', 'BuiltIn', 'Custom'
    :type policy_type: str or
     ~azure.mgmt.resource.policy.v2019_01_01.models.PolicyType
    :param display_name: The display name of the policy set definition.
    :type display_name: str
    :param description: The policy set definition description.
    :type description: str
    :param metadata: The policy set definition metadata.
    :type metadata: object
    :param parameters: The policy set definition parameters that can be used
     in policy definition references.
    :type parameters: object
    :param policy_definitions: Required. An array of policy definition
     references.
    :type policy_definitions:
     list[~azure.mgmt.resource.policy.v2019_01_01.models.PolicyDefinitionReference]
    :ivar id: The ID of the policy set definition.
    :vartype id: str
    :ivar name: The name of the policy set definition.
    :vartype name: str
    :ivar type: The type of the resource
     (Microsoft.Authorization/policySetDefinitions).
    :vartype type: str
    """

    _validation = {
        'policy_definitions': {'required': True},
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'policy_type': {'key': 'properties.policyType', 'type': 'str'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'metadata': {'key': 'properties.metadata', 'type': 'object'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'policy_definitions': {'key': 'properties.policyDefinitions', 'type': '[PolicyDefinitionReference]'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicySetDefinition, self).__init__(**kwargs)
        self.policy_type = kwargs.get('policy_type', None)
        self.display_name = kwargs.get('display_name', None)
        self.description = kwargs.get('description', None)
        self.metadata = kwargs.get('metadata', None)
        self.parameters = kwargs.get('parameters', None)
        self.policy_definitions = kwargs.get('policy_definitions', None)
        self.id = None
        self.name = None
        self.type = None


class PolicySku(Model):
    """The policy sku. This property is optional, obsolete, and will be ignored.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the policy sku. Possible values are A0
     and A1.
    :type name: str
    :param tier: The policy sku tier. Possible values are Free and Standard.
    :type tier: str
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicySku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)
