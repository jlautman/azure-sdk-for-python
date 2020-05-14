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


class NameAvailabilityParameters(Model):
    """Data POST-ed to the nameAvailability action.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. The resource type. Should be always
     "Microsoft.SpoolService/spools".
    :type type: str
    :param name: Required. The Spool service name to validate.
     e.g."my-Spool-name-here"
    :type name: str
    """

    _validation = {
        'type': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, *, type: str, name: str, **kwargs) -> None:
        super(NameAvailabilityParameters, self).__init__(**kwargs)
        self.type = type
        self.name = name
