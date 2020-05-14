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


class SpoolKeys(Model):
    """A class representing the access keys of Spool service.

    :param primary_key: The primary access key.
    :type primary_key: str
    :param secondary_key: The secondary access key.
    :type secondary_key: str
    :param primary_connection_string: Spool connection string constructed via
     the primaryKey
    :type primary_connection_string: str
    :param secondary_connection_string: Spool connection string constructed
     via the secondaryKey
    :type secondary_connection_string: str
    """

    _attribute_map = {
        'primary_key': {'key': 'primaryKey', 'type': 'str'},
        'secondary_key': {'key': 'secondaryKey', 'type': 'str'},
        'primary_connection_string': {'key': 'primaryConnectionString', 'type': 'str'},
        'secondary_connection_string': {'key': 'secondaryConnectionString', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SpoolKeys, self).__init__(**kwargs)
        self.primary_key = kwargs.get('primary_key', None)
        self.secondary_key = kwargs.get('secondary_key', None)
        self.primary_connection_string = kwargs.get('primary_connection_string', None)
        self.secondary_connection_string = kwargs.get('secondary_connection_string', None)
