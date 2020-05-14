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

try:
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .operation_display_py3 import OperationDisplay
    from .dimension_py3 import Dimension
    from .metric_specification_py3 import MetricSpecification
    from .service_specification_py3 import ServiceSpecification
    from .operation_properties_py3 import OperationProperties
    from .operation_py3 import Operation
    from .name_availability_parameters_py3 import NameAvailabilityParameters
    from .name_availability_py3 import NameAvailability
    from .spool_resource_py3 import SpoolResource
    from .resource_py3 import Resource
    from .location_resource_py3 import LocationResource
    from .tagged_resource_py3 import TaggedResource
    from .spool_keys_py3 import SpoolKeys
    from .regenerate_key_parameters_py3 import RegenerateKeyParameters
except (SyntaxError, ImportError):
    from .error_response import ErrorResponse, ErrorResponseException
    from .operation_display import OperationDisplay
    from .dimension import Dimension
    from .metric_specification import MetricSpecification
    from .service_specification import ServiceSpecification
    from .operation_properties import OperationProperties
    from .operation import Operation
    from .name_availability_parameters import NameAvailabilityParameters
    from .name_availability import NameAvailability
    from .spool_resource import SpoolResource
    from .resource import Resource
    from .location_resource import LocationResource
    from .tagged_resource import TaggedResource
    from .spool_keys import SpoolKeys
    from .regenerate_key_parameters import RegenerateKeyParameters
from .operation_paged import OperationPaged
from .spool_resource_paged import SpoolResourcePaged
from .spool_management_client_enums import (
    AggregationType,
    ProvisioningState,
    OptionalFeature,
    KeyType,
)

__all__ = [
    'ErrorResponse', 'ErrorResponseException',
    'OperationDisplay',
    'Dimension',
    'MetricSpecification',
    'ServiceSpecification',
    'OperationProperties',
    'Operation',
    'NameAvailabilityParameters',
    'NameAvailability',
    'SpoolResource',
    'Resource',
    'LocationResource',
    'TaggedResource',
    'SpoolKeys',
    'RegenerateKeyParameters',
    'OperationPaged',
    'SpoolResourcePaged',
    'AggregationType',
    'ProvisioningState',
    'OptionalFeature',
    'KeyType',
]
