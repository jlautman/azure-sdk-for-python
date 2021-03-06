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


class SoftwareUpdateConfigurationRun(Model):
    """Software update configuration Run properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Name of the software update configuration run.
    :vartype name: str
    :ivar id: Resource Id of the software update configuration run
    :vartype id: str
    :param software_update_configuration: software update configuration
     triggered this run
    :type software_update_configuration:
     ~azure.mgmt.automation.models.UpdateConfigurationNavigation
    :ivar status: Status of the software update configuration run.
    :vartype status: str
    :ivar configured_duration: Configured duration for the software update
     configuration run.
    :vartype configured_duration: str
    :ivar os_type: Operating system target of the software update
     configuration triggered this run
    :vartype os_type: str
    :ivar start_time: Start time of the software update configuration run.
    :vartype start_time: datetime
    :ivar end_time: End time of the software update configuration run.
    :vartype end_time: datetime
    :ivar computer_count: Number of computers in the software update
     configuration run.
    :vartype computer_count: int
    :ivar failed_count: Number of computers with failed status.
    :vartype failed_count: int
    :ivar creation_time: Creation time of the resource, which only appears in
     the response.
    :vartype creation_time: datetime
    :ivar created_by: CreatedBy property, which only appears in the response.
    :vartype created_by: str
    :ivar last_modified_time: Last time resource was modified, which only
     appears in the response.
    :vartype last_modified_time: datetime
    :ivar last_modified_by: LastModifiedBy property, which only appears in the
     response.
    :vartype last_modified_by: str
    :param tasks: Software update configuration tasks triggered in this run
    :type tasks:
     ~azure.mgmt.automation.models.SoftareUpdateConfigurationRunTasks
    """

    _validation = {
        'name': {'readonly': True},
        'id': {'readonly': True},
        'status': {'readonly': True},
        'configured_duration': {'readonly': True},
        'os_type': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'computer_count': {'readonly': True},
        'failed_count': {'readonly': True},
        'creation_time': {'readonly': True},
        'created_by': {'readonly': True},
        'last_modified_time': {'readonly': True},
        'last_modified_by': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'id': {'key': 'id', 'type': 'str'},
        'software_update_configuration': {'key': 'properties.softwareUpdateConfiguration', 'type': 'UpdateConfigurationNavigation'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'configured_duration': {'key': 'properties.configuredDuration', 'type': 'str'},
        'os_type': {'key': 'properties.osType', 'type': 'str'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'computer_count': {'key': 'properties.computerCount', 'type': 'int'},
        'failed_count': {'key': 'properties.failedCount', 'type': 'int'},
        'creation_time': {'key': 'properties.creationTime', 'type': 'iso-8601'},
        'created_by': {'key': 'properties.createdBy', 'type': 'str'},
        'last_modified_time': {'key': 'properties.lastModifiedTime', 'type': 'iso-8601'},
        'last_modified_by': {'key': 'properties.lastModifiedBy', 'type': 'str'},
        'tasks': {'key': 'properties.tasks', 'type': 'SoftareUpdateConfigurationRunTasks'},
    }

    def __init__(self, **kwargs):
        super(SoftwareUpdateConfigurationRun, self).__init__(**kwargs)
        self.name = None
        self.id = None
        self.software_update_configuration = kwargs.get('software_update_configuration', None)
        self.status = None
        self.configured_duration = None
        self.os_type = None
        self.start_time = None
        self.end_time = None
        self.computer_count = None
        self.failed_count = None
        self.creation_time = None
        self.created_by = None
        self.last_modified_time = None
        self.last_modified_by = None
        self.tasks = kwargs.get('tasks', None)
