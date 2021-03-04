# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1DataVolumeSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'checkpoints': 'list[V1alpha1DataVolumeCheckpoint]',
        'content_type': 'str',
        'final_checkpoint': 'bool',
        'preallocation': 'bool',
        'pvc': 'K8sIoApiCoreV1PersistentVolumeClaimSpec',
        'source': 'V1alpha1DataVolumeSource'
    }

    attribute_map = {
        'checkpoints': 'checkpoints',
        'content_type': 'contentType',
        'final_checkpoint': 'finalCheckpoint',
        'preallocation': 'preallocation',
        'pvc': 'pvc',
        'source': 'source'
    }

    def __init__(self, checkpoints=None, content_type=None, final_checkpoint=None, preallocation=None, pvc=None, source=None):
        """
        V1alpha1DataVolumeSpec - a model defined in Swagger
        """

        self._checkpoints = None
        self._content_type = None
        self._final_checkpoint = None
        self._preallocation = None
        self._pvc = None
        self._source = None

        if checkpoints is not None:
          self.checkpoints = checkpoints
        if content_type is not None:
          self.content_type = content_type
        if final_checkpoint is not None:
          self.final_checkpoint = final_checkpoint
        if preallocation is not None:
          self.preallocation = preallocation
        self.pvc = pvc
        self.source = source

    @property
    def checkpoints(self):
        """
        Gets the checkpoints of this V1alpha1DataVolumeSpec.
        Checkpoints is a list of DataVolumeCheckpoints, representing stages in a multistage import.

        :return: The checkpoints of this V1alpha1DataVolumeSpec.
        :rtype: list[V1alpha1DataVolumeCheckpoint]
        """
        return self._checkpoints

    @checkpoints.setter
    def checkpoints(self, checkpoints):
        """
        Sets the checkpoints of this V1alpha1DataVolumeSpec.
        Checkpoints is a list of DataVolumeCheckpoints, representing stages in a multistage import.

        :param checkpoints: The checkpoints of this V1alpha1DataVolumeSpec.
        :type: list[V1alpha1DataVolumeCheckpoint]
        """

        self._checkpoints = checkpoints

    @property
    def content_type(self):
        """
        Gets the content_type of this V1alpha1DataVolumeSpec.
        DataVolumeContentType options: \"kubevirt\", \"archive\"

        :return: The content_type of this V1alpha1DataVolumeSpec.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """
        Sets the content_type of this V1alpha1DataVolumeSpec.
        DataVolumeContentType options: \"kubevirt\", \"archive\"

        :param content_type: The content_type of this V1alpha1DataVolumeSpec.
        :type: str
        """

        self._content_type = content_type

    @property
    def final_checkpoint(self):
        """
        Gets the final_checkpoint of this V1alpha1DataVolumeSpec.
        FinalCheckpoint indicates whether the current DataVolumeCheckpoint is the final checkpoint.

        :return: The final_checkpoint of this V1alpha1DataVolumeSpec.
        :rtype: bool
        """
        return self._final_checkpoint

    @final_checkpoint.setter
    def final_checkpoint(self, final_checkpoint):
        """
        Sets the final_checkpoint of this V1alpha1DataVolumeSpec.
        FinalCheckpoint indicates whether the current DataVolumeCheckpoint is the final checkpoint.

        :param final_checkpoint: The final_checkpoint of this V1alpha1DataVolumeSpec.
        :type: bool
        """

        self._final_checkpoint = final_checkpoint

    @property
    def preallocation(self):
        """
        Gets the preallocation of this V1alpha1DataVolumeSpec.
        Preallocation controls whether storage for DataVolumes should be allocated in advance.

        :return: The preallocation of this V1alpha1DataVolumeSpec.
        :rtype: bool
        """
        return self._preallocation

    @preallocation.setter
    def preallocation(self, preallocation):
        """
        Sets the preallocation of this V1alpha1DataVolumeSpec.
        Preallocation controls whether storage for DataVolumes should be allocated in advance.

        :param preallocation: The preallocation of this V1alpha1DataVolumeSpec.
        :type: bool
        """

        self._preallocation = preallocation

    @property
    def pvc(self):
        """
        Gets the pvc of this V1alpha1DataVolumeSpec.
        PVC is the PVC specification

        :return: The pvc of this V1alpha1DataVolumeSpec.
        :rtype: K8sIoApiCoreV1PersistentVolumeClaimSpec
        """
        return self._pvc

    @pvc.setter
    def pvc(self, pvc):
        """
        Sets the pvc of this V1alpha1DataVolumeSpec.
        PVC is the PVC specification

        :param pvc: The pvc of this V1alpha1DataVolumeSpec.
        :type: K8sIoApiCoreV1PersistentVolumeClaimSpec
        """
        if pvc is None:
            raise ValueError("Invalid value for `pvc`, must not be `None`")

        self._pvc = pvc

    @property
    def source(self):
        """
        Gets the source of this V1alpha1DataVolumeSpec.
        Source is the src of the data for the requested DataVolume

        :return: The source of this V1alpha1DataVolumeSpec.
        :rtype: V1alpha1DataVolumeSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this V1alpha1DataVolumeSpec.
        Source is the src of the data for the requested DataVolume

        :param source: The source of this V1alpha1DataVolumeSpec.
        :type: V1alpha1DataVolumeSource
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")

        self._source = source

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1DataVolumeSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
