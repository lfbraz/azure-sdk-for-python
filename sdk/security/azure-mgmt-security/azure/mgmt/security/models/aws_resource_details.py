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

from .resource_details import ResourceDetails


class AwsResourceDetails(ResourceDetails):
    """Details of the resource that was assessed.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param source: Required. Constant filled by server.
    :type source: str
    :ivar account_id: AWS account ID
    :vartype account_id: str
    :ivar aws_resource_id: AWS resource ID. can be ARN or other
    :vartype aws_resource_id: str
    """

    _validation = {
        'source': {'required': True},
        'account_id': {'readonly': True},
        'aws_resource_id': {'readonly': True},
    }

    _attribute_map = {
        'source': {'key': 'source', 'type': 'str'},
        'account_id': {'key': 'accountId', 'type': 'str'},
        'aws_resource_id': {'key': 'awsResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AwsResourceDetails, self).__init__(**kwargs)
        self.account_id = None
        self.aws_resource_id = None
        self.source = 'Aws'