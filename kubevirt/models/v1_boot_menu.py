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


class V1BootMenu(object):
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
        'enabled': 'bool',
        'timeout': 'int'
    }

    attribute_map = {
        'enabled': 'enabled',
        'timeout': 'timeout'
    }

    def __init__(self, enabled=None, timeout=None):
        """
        V1BootMenu - a model defined in Swagger
        """

        self._enabled = None
        self._timeout = None

        if enabled is not None:
          self.enabled = enabled
        if timeout is not None:
          self.timeout = timeout

    @property
    def enabled(self):
        """
        Gets the enabled of this V1BootMenu.

        :return: The enabled of this V1BootMenu.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """
        Sets the enabled of this V1BootMenu.

        :param enabled: The enabled of this V1BootMenu.
        :type: bool
        """

        self._enabled = enabled

    @property
    def timeout(self):
        """
        Gets the timeout of this V1BootMenu.

        :return: The timeout of this V1BootMenu.
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets the timeout of this V1BootMenu.

        :param timeout: The timeout of this V1BootMenu.
        :type: int
        """

        self._timeout = timeout

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
        if not isinstance(other, V1BootMenu):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
