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


class Emotion(Model):
    """Properties describing facial emotion in form of confidence ranging from 0
    to 1.

    :param anger:
    :type anger: float
    :param contempt:
    :type contempt: float
    :param disgust:
    :type disgust: float
    :param fear:
    :type fear: float
    :param happiness:
    :type happiness: float
    :param neutral:
    :type neutral: float
    :param sadness:
    :type sadness: float
    :param surprise:
    :type surprise: float
    """

    _attribute_map = {
        'anger': {'key': 'anger', 'type': 'float'},
        'contempt': {'key': 'contempt', 'type': 'float'},
        'disgust': {'key': 'disgust', 'type': 'float'},
        'fear': {'key': 'fear', 'type': 'float'},
        'happiness': {'key': 'happiness', 'type': 'float'},
        'neutral': {'key': 'neutral', 'type': 'float'},
        'sadness': {'key': 'sadness', 'type': 'float'},
        'surprise': {'key': 'surprise', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(Emotion, self).__init__(**kwargs)
        self.anger = kwargs.get('anger', None)
        self.contempt = kwargs.get('contempt', None)
        self.disgust = kwargs.get('disgust', None)
        self.fear = kwargs.get('fear', None)
        self.happiness = kwargs.get('happiness', None)
        self.neutral = kwargs.get('neutral', None)
        self.sadness = kwargs.get('sadness', None)
        self.surprise = kwargs.get('surprise', None)