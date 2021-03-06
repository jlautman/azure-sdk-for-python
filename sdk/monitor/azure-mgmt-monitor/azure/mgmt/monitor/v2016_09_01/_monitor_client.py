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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import MonitorClientConfiguration
from .operations import MetricsOperations
from .operations import ServiceDiagnosticSettingsOperations
from . import models


class MonitorClient(SDKClient):
    """Monitor Management Client

    :ivar config: Configuration for client.
    :vartype config: MonitorClientConfiguration

    :ivar metrics: Metrics operations
    :vartype metrics: azure.mgmt.monitor.v2016_09_01.operations.MetricsOperations
    :ivar service_diagnostic_settings: ServiceDiagnosticSettings operations
    :vartype service_diagnostic_settings: azure.mgmt.monitor.v2016_09_01.operations.ServiceDiagnosticSettingsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = MonitorClientConfiguration(credentials, base_url)
        super(MonitorClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2016-09-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.metrics = MetricsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service_diagnostic_settings = ServiceDiagnosticSettingsOperations(
            self._client, self.config, self._serialize, self._deserialize)
