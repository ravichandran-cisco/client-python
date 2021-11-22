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


class V1UnpauseOptions(object):
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
        'api_version': 'str',
        'dry_run': 'list[str]',
        'kind': 'str'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'dry_run': 'dryRun',
        'kind': 'kind'
    }

    def __init__(self, api_version=None, dry_run=None, kind=None):
        """
        V1UnpauseOptions - a model defined in Swagger
        """

        self._api_version = None
        self._dry_run = None
        self._kind = None

        if api_version is not None:
          self.api_version = api_version
        if dry_run is not None:
          self.dry_run = dry_run
        if kind is not None:
          self.kind = kind

    @property
    def api_version(self):
        """
        Gets the api_version of this V1UnpauseOptions.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

        :return: The api_version of this V1UnpauseOptions.
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api_version of this V1UnpauseOptions.
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

        :param api_version: The api_version of this V1UnpauseOptions.
        :type: str
        """

        self._api_version = api_version

    @property
    def dry_run(self):
        """
        Gets the dry_run of this V1UnpauseOptions.
        When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed

        :return: The dry_run of this V1UnpauseOptions.
        :rtype: list[str]
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """
        Sets the dry_run of this V1UnpauseOptions.
        When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed

        :param dry_run: The dry_run of this V1UnpauseOptions.
        :type: list[str]
        """

        self._dry_run = dry_run

    @property
    def kind(self):
        """
        Gets the kind of this V1UnpauseOptions.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

        :return: The kind of this V1UnpauseOptions.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this V1UnpauseOptions.
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

        :param kind: The kind of this V1UnpauseOptions.
        :type: str
        """

        self._kind = kind

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
        if not isinstance(other, V1UnpauseOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
