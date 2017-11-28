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


class V1Disk(object):
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
        'auth': 'V1DiskAuth',
        'cloudinit': 'V1CloudInitSpec',
        'device': 'str',
        'driver': 'V1DiskDriver',
        'read_only': 'V1ReadOnly',
        'serial': 'str',
        'snapshot': 'str',
        'source': 'V1DiskSource',
        'target': 'V1DiskTarget',
        'type': 'str'
    }

    attribute_map = {
        'auth': 'auth',
        'cloudinit': 'cloudinit',
        'device': 'device',
        'driver': 'driver',
        'read_only': 'readOnly',
        'serial': 'serial',
        'snapshot': 'snapshot',
        'source': 'source',
        'target': 'target',
        'type': 'type'
    }

    def __init__(self, auth=None, cloudinit=None, device=None, driver=None, read_only=None, serial=None, snapshot=None, source=None, target=None, type=None):
        """
        V1Disk - a model defined in Swagger
        """

        self._auth = None
        self._cloudinit = None
        self._device = None
        self._driver = None
        self._read_only = None
        self._serial = None
        self._snapshot = None
        self._source = None
        self._target = None
        self._type = None

        if auth is not None:
          self.auth = auth
        if cloudinit is not None:
          self.cloudinit = cloudinit
        if device is not None:
          self.device = device
        if driver is not None:
          self.driver = driver
        if read_only is not None:
          self.read_only = read_only
        if serial is not None:
          self.serial = serial
        if snapshot is not None:
          self.snapshot = snapshot
        if source is not None:
          self.source = source
        self.target = target
        self.type = type

    @property
    def auth(self):
        """
        Gets the auth of this V1Disk.

        :return: The auth of this V1Disk.
        :rtype: V1DiskAuth
        """
        return self._auth

    @auth.setter
    def auth(self, auth):
        """
        Sets the auth of this V1Disk.

        :param auth: The auth of this V1Disk.
        :type: V1DiskAuth
        """

        self._auth = auth

    @property
    def cloudinit(self):
        """
        Gets the cloudinit of this V1Disk.

        :return: The cloudinit of this V1Disk.
        :rtype: V1CloudInitSpec
        """
        return self._cloudinit

    @cloudinit.setter
    def cloudinit(self, cloudinit):
        """
        Sets the cloudinit of this V1Disk.

        :param cloudinit: The cloudinit of this V1Disk.
        :type: V1CloudInitSpec
        """

        self._cloudinit = cloudinit

    @property
    def device(self):
        """
        Gets the device of this V1Disk.

        :return: The device of this V1Disk.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """
        Sets the device of this V1Disk.

        :param device: The device of this V1Disk.
        :type: str
        """

        self._device = device

    @property
    def driver(self):
        """
        Gets the driver of this V1Disk.

        :return: The driver of this V1Disk.
        :rtype: V1DiskDriver
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """
        Sets the driver of this V1Disk.

        :param driver: The driver of this V1Disk.
        :type: V1DiskDriver
        """

        self._driver = driver

    @property
    def read_only(self):
        """
        Gets the read_only of this V1Disk.

        :return: The read_only of this V1Disk.
        :rtype: V1ReadOnly
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """
        Sets the read_only of this V1Disk.

        :param read_only: The read_only of this V1Disk.
        :type: V1ReadOnly
        """

        self._read_only = read_only

    @property
    def serial(self):
        """
        Gets the serial of this V1Disk.

        :return: The serial of this V1Disk.
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """
        Sets the serial of this V1Disk.

        :param serial: The serial of this V1Disk.
        :type: str
        """

        self._serial = serial

    @property
    def snapshot(self):
        """
        Gets the snapshot of this V1Disk.

        :return: The snapshot of this V1Disk.
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """
        Sets the snapshot of this V1Disk.

        :param snapshot: The snapshot of this V1Disk.
        :type: str
        """

        self._snapshot = snapshot

    @property
    def source(self):
        """
        Gets the source of this V1Disk.

        :return: The source of this V1Disk.
        :rtype: V1DiskSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this V1Disk.

        :param source: The source of this V1Disk.
        :type: V1DiskSource
        """

        self._source = source

    @property
    def target(self):
        """
        Gets the target of this V1Disk.

        :return: The target of this V1Disk.
        :rtype: V1DiskTarget
        """
        return self._target

    @target.setter
    def target(self, target):
        """
        Sets the target of this V1Disk.

        :param target: The target of this V1Disk.
        :type: V1DiskTarget
        """
        if target is None:
            raise ValueError("Invalid value for `target`, must not be `None`")

        self._target = target

    @property
    def type(self):
        """
        Gets the type of this V1Disk.

        :return: The type of this V1Disk.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1Disk.

        :param type: The type of this V1Disk.
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if not isinstance(other, V1Disk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
