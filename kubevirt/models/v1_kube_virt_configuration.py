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


class V1KubeVirtConfiguration(object):
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
        'additional_guest_memory_overhead_ratio': 'str',
        'api_configuration': 'V1ReloadableComponentConfiguration',
        'controller_configuration': 'V1ReloadableComponentConfiguration',
        'cpu_model': 'str',
        'cpu_request': 'K8sIoApimachineryPkgApiResourceQuantity',
        'default_runtime_class': 'str',
        'developer_configuration': 'V1DeveloperConfiguration',
        'emulated_machines': 'list[str]',
        'eviction_strategy': 'str',
        'handler_configuration': 'V1ReloadableComponentConfiguration',
        'image_pull_policy': 'str',
        'machine_type': 'str',
        'mediated_devices_configuration': 'V1MediatedDevicesConfiguration',
        'mem_balloon_stats_period': 'int',
        'migrations': 'V1MigrationConfiguration',
        'min_cpu_model': 'str',
        'network': 'V1NetworkConfiguration',
        'obsolete_cpu_models': 'dict(str, bool)',
        'ovmf_path': 'str',
        'permitted_host_devices': 'V1PermittedHostDevices',
        'seccomp_configuration': 'V1SeccompConfiguration',
        'selinux_launcher_type': 'str',
        'smbios': 'V1SMBiosConfiguration',
        'supported_guest_agent_versions': 'list[str]',
        'tls_configuration': 'V1TLSConfiguration',
        'virtual_machine_instances_per_node': 'int',
        'webhook_configuration': 'V1ReloadableComponentConfiguration'
    }

    attribute_map = {
        'additional_guest_memory_overhead_ratio': 'additionalGuestMemoryOverheadRatio',
        'api_configuration': 'apiConfiguration',
        'controller_configuration': 'controllerConfiguration',
        'cpu_model': 'cpuModel',
        'cpu_request': 'cpuRequest',
        'default_runtime_class': 'defaultRuntimeClass',
        'developer_configuration': 'developerConfiguration',
        'emulated_machines': 'emulatedMachines',
        'eviction_strategy': 'evictionStrategy',
        'handler_configuration': 'handlerConfiguration',
        'image_pull_policy': 'imagePullPolicy',
        'machine_type': 'machineType',
        'mediated_devices_configuration': 'mediatedDevicesConfiguration',
        'mem_balloon_stats_period': 'memBalloonStatsPeriod',
        'migrations': 'migrations',
        'min_cpu_model': 'minCPUModel',
        'network': 'network',
        'obsolete_cpu_models': 'obsoleteCPUModels',
        'ovmf_path': 'ovmfPath',
        'permitted_host_devices': 'permittedHostDevices',
        'seccomp_configuration': 'seccompConfiguration',
        'selinux_launcher_type': 'selinuxLauncherType',
        'smbios': 'smbios',
        'supported_guest_agent_versions': 'supportedGuestAgentVersions',
        'tls_configuration': 'tlsConfiguration',
        'virtual_machine_instances_per_node': 'virtualMachineInstancesPerNode',
        'webhook_configuration': 'webhookConfiguration'
    }

    def __init__(self, additional_guest_memory_overhead_ratio=None, api_configuration=None, controller_configuration=None, cpu_model=None, cpu_request=None, default_runtime_class=None, developer_configuration=None, emulated_machines=None, eviction_strategy=None, handler_configuration=None, image_pull_policy=None, machine_type=None, mediated_devices_configuration=None, mem_balloon_stats_period=None, migrations=None, min_cpu_model=None, network=None, obsolete_cpu_models=None, ovmf_path=None, permitted_host_devices=None, seccomp_configuration=None, selinux_launcher_type=None, smbios=None, supported_guest_agent_versions=None, tls_configuration=None, virtual_machine_instances_per_node=None, webhook_configuration=None):
        """
        V1KubeVirtConfiguration - a model defined in Swagger
        """

        self._additional_guest_memory_overhead_ratio = None
        self._api_configuration = None
        self._controller_configuration = None
        self._cpu_model = None
        self._cpu_request = None
        self._default_runtime_class = None
        self._developer_configuration = None
        self._emulated_machines = None
        self._eviction_strategy = None
        self._handler_configuration = None
        self._image_pull_policy = None
        self._machine_type = None
        self._mediated_devices_configuration = None
        self._mem_balloon_stats_period = None
        self._migrations = None
        self._min_cpu_model = None
        self._network = None
        self._obsolete_cpu_models = None
        self._ovmf_path = None
        self._permitted_host_devices = None
        self._seccomp_configuration = None
        self._selinux_launcher_type = None
        self._smbios = None
        self._supported_guest_agent_versions = None
        self._tls_configuration = None
        self._virtual_machine_instances_per_node = None
        self._webhook_configuration = None

        if additional_guest_memory_overhead_ratio is not None:
          self.additional_guest_memory_overhead_ratio = additional_guest_memory_overhead_ratio
        if api_configuration is not None:
          self.api_configuration = api_configuration
        if controller_configuration is not None:
          self.controller_configuration = controller_configuration
        if cpu_model is not None:
          self.cpu_model = cpu_model
        if cpu_request is not None:
          self.cpu_request = cpu_request
        if default_runtime_class is not None:
          self.default_runtime_class = default_runtime_class
        if developer_configuration is not None:
          self.developer_configuration = developer_configuration
        if emulated_machines is not None:
          self.emulated_machines = emulated_machines
        if eviction_strategy is not None:
          self.eviction_strategy = eviction_strategy
        if handler_configuration is not None:
          self.handler_configuration = handler_configuration
        if image_pull_policy is not None:
          self.image_pull_policy = image_pull_policy
        if machine_type is not None:
          self.machine_type = machine_type
        if mediated_devices_configuration is not None:
          self.mediated_devices_configuration = mediated_devices_configuration
        if mem_balloon_stats_period is not None:
          self.mem_balloon_stats_period = mem_balloon_stats_period
        if migrations is not None:
          self.migrations = migrations
        if min_cpu_model is not None:
          self.min_cpu_model = min_cpu_model
        if network is not None:
          self.network = network
        if obsolete_cpu_models is not None:
          self.obsolete_cpu_models = obsolete_cpu_models
        if ovmf_path is not None:
          self.ovmf_path = ovmf_path
        if permitted_host_devices is not None:
          self.permitted_host_devices = permitted_host_devices
        if seccomp_configuration is not None:
          self.seccomp_configuration = seccomp_configuration
        if selinux_launcher_type is not None:
          self.selinux_launcher_type = selinux_launcher_type
        if smbios is not None:
          self.smbios = smbios
        if supported_guest_agent_versions is not None:
          self.supported_guest_agent_versions = supported_guest_agent_versions
        if tls_configuration is not None:
          self.tls_configuration = tls_configuration
        if virtual_machine_instances_per_node is not None:
          self.virtual_machine_instances_per_node = virtual_machine_instances_per_node
        if webhook_configuration is not None:
          self.webhook_configuration = webhook_configuration

    @property
    def additional_guest_memory_overhead_ratio(self):
        """
        Gets the additional_guest_memory_overhead_ratio of this V1KubeVirtConfiguration.
        AdditionalGuestMemoryOverheadRatio can be used to increase the virtualization infrastructure overhead. This is useful, since the calculation of this overhead is not accurate and cannot be entirely known in advance. The ratio that is being set determines by which factor to increase the overhead calculated by Kubevirt. A higher ratio means that the VMs would be less compromised by node pressures, but would mean that fewer VMs could be scheduled to a node. If not set, the default is 1.

        :return: The additional_guest_memory_overhead_ratio of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._additional_guest_memory_overhead_ratio

    @additional_guest_memory_overhead_ratio.setter
    def additional_guest_memory_overhead_ratio(self, additional_guest_memory_overhead_ratio):
        """
        Sets the additional_guest_memory_overhead_ratio of this V1KubeVirtConfiguration.
        AdditionalGuestMemoryOverheadRatio can be used to increase the virtualization infrastructure overhead. This is useful, since the calculation of this overhead is not accurate and cannot be entirely known in advance. The ratio that is being set determines by which factor to increase the overhead calculated by Kubevirt. A higher ratio means that the VMs would be less compromised by node pressures, but would mean that fewer VMs could be scheduled to a node. If not set, the default is 1.

        :param additional_guest_memory_overhead_ratio: The additional_guest_memory_overhead_ratio of this V1KubeVirtConfiguration.
        :type: str
        """

        self._additional_guest_memory_overhead_ratio = additional_guest_memory_overhead_ratio

    @property
    def api_configuration(self):
        """
        Gets the api_configuration of this V1KubeVirtConfiguration.

        :return: The api_configuration of this V1KubeVirtConfiguration.
        :rtype: V1ReloadableComponentConfiguration
        """
        return self._api_configuration

    @api_configuration.setter
    def api_configuration(self, api_configuration):
        """
        Sets the api_configuration of this V1KubeVirtConfiguration.

        :param api_configuration: The api_configuration of this V1KubeVirtConfiguration.
        :type: V1ReloadableComponentConfiguration
        """

        self._api_configuration = api_configuration

    @property
    def controller_configuration(self):
        """
        Gets the controller_configuration of this V1KubeVirtConfiguration.

        :return: The controller_configuration of this V1KubeVirtConfiguration.
        :rtype: V1ReloadableComponentConfiguration
        """
        return self._controller_configuration

    @controller_configuration.setter
    def controller_configuration(self, controller_configuration):
        """
        Sets the controller_configuration of this V1KubeVirtConfiguration.

        :param controller_configuration: The controller_configuration of this V1KubeVirtConfiguration.
        :type: V1ReloadableComponentConfiguration
        """

        self._controller_configuration = controller_configuration

    @property
    def cpu_model(self):
        """
        Gets the cpu_model of this V1KubeVirtConfiguration.

        :return: The cpu_model of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """
        Sets the cpu_model of this V1KubeVirtConfiguration.

        :param cpu_model: The cpu_model of this V1KubeVirtConfiguration.
        :type: str
        """

        self._cpu_model = cpu_model

    @property
    def cpu_request(self):
        """
        Gets the cpu_request of this V1KubeVirtConfiguration.

        :return: The cpu_request of this V1KubeVirtConfiguration.
        :rtype: K8sIoApimachineryPkgApiResourceQuantity
        """
        return self._cpu_request

    @cpu_request.setter
    def cpu_request(self, cpu_request):
        """
        Sets the cpu_request of this V1KubeVirtConfiguration.

        :param cpu_request: The cpu_request of this V1KubeVirtConfiguration.
        :type: K8sIoApimachineryPkgApiResourceQuantity
        """

        self._cpu_request = cpu_request

    @property
    def default_runtime_class(self):
        """
        Gets the default_runtime_class of this V1KubeVirtConfiguration.

        :return: The default_runtime_class of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._default_runtime_class

    @default_runtime_class.setter
    def default_runtime_class(self, default_runtime_class):
        """
        Sets the default_runtime_class of this V1KubeVirtConfiguration.

        :param default_runtime_class: The default_runtime_class of this V1KubeVirtConfiguration.
        :type: str
        """

        self._default_runtime_class = default_runtime_class

    @property
    def developer_configuration(self):
        """
        Gets the developer_configuration of this V1KubeVirtConfiguration.

        :return: The developer_configuration of this V1KubeVirtConfiguration.
        :rtype: V1DeveloperConfiguration
        """
        return self._developer_configuration

    @developer_configuration.setter
    def developer_configuration(self, developer_configuration):
        """
        Sets the developer_configuration of this V1KubeVirtConfiguration.

        :param developer_configuration: The developer_configuration of this V1KubeVirtConfiguration.
        :type: V1DeveloperConfiguration
        """

        self._developer_configuration = developer_configuration

    @property
    def emulated_machines(self):
        """
        Gets the emulated_machines of this V1KubeVirtConfiguration.

        :return: The emulated_machines of this V1KubeVirtConfiguration.
        :rtype: list[str]
        """
        return self._emulated_machines

    @emulated_machines.setter
    def emulated_machines(self, emulated_machines):
        """
        Sets the emulated_machines of this V1KubeVirtConfiguration.

        :param emulated_machines: The emulated_machines of this V1KubeVirtConfiguration.
        :type: list[str]
        """

        self._emulated_machines = emulated_machines

    @property
    def eviction_strategy(self):
        """
        Gets the eviction_strategy of this V1KubeVirtConfiguration.
        EvictionStrategy defines at the cluster level if the VirtualMachineInstance should be migrated instead of shut-off in case of a node drain. If the VirtualMachineInstance specific field is set it overrides the cluster level one.

        :return: The eviction_strategy of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._eviction_strategy

    @eviction_strategy.setter
    def eviction_strategy(self, eviction_strategy):
        """
        Sets the eviction_strategy of this V1KubeVirtConfiguration.
        EvictionStrategy defines at the cluster level if the VirtualMachineInstance should be migrated instead of shut-off in case of a node drain. If the VirtualMachineInstance specific field is set it overrides the cluster level one.

        :param eviction_strategy: The eviction_strategy of this V1KubeVirtConfiguration.
        :type: str
        """

        self._eviction_strategy = eviction_strategy

    @property
    def handler_configuration(self):
        """
        Gets the handler_configuration of this V1KubeVirtConfiguration.

        :return: The handler_configuration of this V1KubeVirtConfiguration.
        :rtype: V1ReloadableComponentConfiguration
        """
        return self._handler_configuration

    @handler_configuration.setter
    def handler_configuration(self, handler_configuration):
        """
        Sets the handler_configuration of this V1KubeVirtConfiguration.

        :param handler_configuration: The handler_configuration of this V1KubeVirtConfiguration.
        :type: V1ReloadableComponentConfiguration
        """

        self._handler_configuration = handler_configuration

    @property
    def image_pull_policy(self):
        """
        Gets the image_pull_policy of this V1KubeVirtConfiguration.

        :return: The image_pull_policy of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._image_pull_policy

    @image_pull_policy.setter
    def image_pull_policy(self, image_pull_policy):
        """
        Sets the image_pull_policy of this V1KubeVirtConfiguration.

        :param image_pull_policy: The image_pull_policy of this V1KubeVirtConfiguration.
        :type: str
        """

        self._image_pull_policy = image_pull_policy

    @property
    def machine_type(self):
        """
        Gets the machine_type of this V1KubeVirtConfiguration.

        :return: The machine_type of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._machine_type

    @machine_type.setter
    def machine_type(self, machine_type):
        """
        Sets the machine_type of this V1KubeVirtConfiguration.

        :param machine_type: The machine_type of this V1KubeVirtConfiguration.
        :type: str
        """

        self._machine_type = machine_type

    @property
    def mediated_devices_configuration(self):
        """
        Gets the mediated_devices_configuration of this V1KubeVirtConfiguration.

        :return: The mediated_devices_configuration of this V1KubeVirtConfiguration.
        :rtype: V1MediatedDevicesConfiguration
        """
        return self._mediated_devices_configuration

    @mediated_devices_configuration.setter
    def mediated_devices_configuration(self, mediated_devices_configuration):
        """
        Sets the mediated_devices_configuration of this V1KubeVirtConfiguration.

        :param mediated_devices_configuration: The mediated_devices_configuration of this V1KubeVirtConfiguration.
        :type: V1MediatedDevicesConfiguration
        """

        self._mediated_devices_configuration = mediated_devices_configuration

    @property
    def mem_balloon_stats_period(self):
        """
        Gets the mem_balloon_stats_period of this V1KubeVirtConfiguration.

        :return: The mem_balloon_stats_period of this V1KubeVirtConfiguration.
        :rtype: int
        """
        return self._mem_balloon_stats_period

    @mem_balloon_stats_period.setter
    def mem_balloon_stats_period(self, mem_balloon_stats_period):
        """
        Sets the mem_balloon_stats_period of this V1KubeVirtConfiguration.

        :param mem_balloon_stats_period: The mem_balloon_stats_period of this V1KubeVirtConfiguration.
        :type: int
        """

        self._mem_balloon_stats_period = mem_balloon_stats_period

    @property
    def migrations(self):
        """
        Gets the migrations of this V1KubeVirtConfiguration.

        :return: The migrations of this V1KubeVirtConfiguration.
        :rtype: V1MigrationConfiguration
        """
        return self._migrations

    @migrations.setter
    def migrations(self, migrations):
        """
        Sets the migrations of this V1KubeVirtConfiguration.

        :param migrations: The migrations of this V1KubeVirtConfiguration.
        :type: V1MigrationConfiguration
        """

        self._migrations = migrations

    @property
    def min_cpu_model(self):
        """
        Gets the min_cpu_model of this V1KubeVirtConfiguration.

        :return: The min_cpu_model of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._min_cpu_model

    @min_cpu_model.setter
    def min_cpu_model(self, min_cpu_model):
        """
        Sets the min_cpu_model of this V1KubeVirtConfiguration.

        :param min_cpu_model: The min_cpu_model of this V1KubeVirtConfiguration.
        :type: str
        """

        self._min_cpu_model = min_cpu_model

    @property
    def network(self):
        """
        Gets the network of this V1KubeVirtConfiguration.

        :return: The network of this V1KubeVirtConfiguration.
        :rtype: V1NetworkConfiguration
        """
        return self._network

    @network.setter
    def network(self, network):
        """
        Sets the network of this V1KubeVirtConfiguration.

        :param network: The network of this V1KubeVirtConfiguration.
        :type: V1NetworkConfiguration
        """

        self._network = network

    @property
    def obsolete_cpu_models(self):
        """
        Gets the obsolete_cpu_models of this V1KubeVirtConfiguration.

        :return: The obsolete_cpu_models of this V1KubeVirtConfiguration.
        :rtype: dict(str, bool)
        """
        return self._obsolete_cpu_models

    @obsolete_cpu_models.setter
    def obsolete_cpu_models(self, obsolete_cpu_models):
        """
        Sets the obsolete_cpu_models of this V1KubeVirtConfiguration.

        :param obsolete_cpu_models: The obsolete_cpu_models of this V1KubeVirtConfiguration.
        :type: dict(str, bool)
        """

        self._obsolete_cpu_models = obsolete_cpu_models

    @property
    def ovmf_path(self):
        """
        Gets the ovmf_path of this V1KubeVirtConfiguration.

        :return: The ovmf_path of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._ovmf_path

    @ovmf_path.setter
    def ovmf_path(self, ovmf_path):
        """
        Sets the ovmf_path of this V1KubeVirtConfiguration.

        :param ovmf_path: The ovmf_path of this V1KubeVirtConfiguration.
        :type: str
        """

        self._ovmf_path = ovmf_path

    @property
    def permitted_host_devices(self):
        """
        Gets the permitted_host_devices of this V1KubeVirtConfiguration.

        :return: The permitted_host_devices of this V1KubeVirtConfiguration.
        :rtype: V1PermittedHostDevices
        """
        return self._permitted_host_devices

    @permitted_host_devices.setter
    def permitted_host_devices(self, permitted_host_devices):
        """
        Sets the permitted_host_devices of this V1KubeVirtConfiguration.

        :param permitted_host_devices: The permitted_host_devices of this V1KubeVirtConfiguration.
        :type: V1PermittedHostDevices
        """

        self._permitted_host_devices = permitted_host_devices

    @property
    def seccomp_configuration(self):
        """
        Gets the seccomp_configuration of this V1KubeVirtConfiguration.

        :return: The seccomp_configuration of this V1KubeVirtConfiguration.
        :rtype: V1SeccompConfiguration
        """
        return self._seccomp_configuration

    @seccomp_configuration.setter
    def seccomp_configuration(self, seccomp_configuration):
        """
        Sets the seccomp_configuration of this V1KubeVirtConfiguration.

        :param seccomp_configuration: The seccomp_configuration of this V1KubeVirtConfiguration.
        :type: V1SeccompConfiguration
        """

        self._seccomp_configuration = seccomp_configuration

    @property
    def selinux_launcher_type(self):
        """
        Gets the selinux_launcher_type of this V1KubeVirtConfiguration.

        :return: The selinux_launcher_type of this V1KubeVirtConfiguration.
        :rtype: str
        """
        return self._selinux_launcher_type

    @selinux_launcher_type.setter
    def selinux_launcher_type(self, selinux_launcher_type):
        """
        Sets the selinux_launcher_type of this V1KubeVirtConfiguration.

        :param selinux_launcher_type: The selinux_launcher_type of this V1KubeVirtConfiguration.
        :type: str
        """

        self._selinux_launcher_type = selinux_launcher_type

    @property
    def smbios(self):
        """
        Gets the smbios of this V1KubeVirtConfiguration.

        :return: The smbios of this V1KubeVirtConfiguration.
        :rtype: V1SMBiosConfiguration
        """
        return self._smbios

    @smbios.setter
    def smbios(self, smbios):
        """
        Sets the smbios of this V1KubeVirtConfiguration.

        :param smbios: The smbios of this V1KubeVirtConfiguration.
        :type: V1SMBiosConfiguration
        """

        self._smbios = smbios

    @property
    def supported_guest_agent_versions(self):
        """
        Gets the supported_guest_agent_versions of this V1KubeVirtConfiguration.
        deprecated

        :return: The supported_guest_agent_versions of this V1KubeVirtConfiguration.
        :rtype: list[str]
        """
        return self._supported_guest_agent_versions

    @supported_guest_agent_versions.setter
    def supported_guest_agent_versions(self, supported_guest_agent_versions):
        """
        Sets the supported_guest_agent_versions of this V1KubeVirtConfiguration.
        deprecated

        :param supported_guest_agent_versions: The supported_guest_agent_versions of this V1KubeVirtConfiguration.
        :type: list[str]
        """

        self._supported_guest_agent_versions = supported_guest_agent_versions

    @property
    def tls_configuration(self):
        """
        Gets the tls_configuration of this V1KubeVirtConfiguration.

        :return: The tls_configuration of this V1KubeVirtConfiguration.
        :rtype: V1TLSConfiguration
        """
        return self._tls_configuration

    @tls_configuration.setter
    def tls_configuration(self, tls_configuration):
        """
        Sets the tls_configuration of this V1KubeVirtConfiguration.

        :param tls_configuration: The tls_configuration of this V1KubeVirtConfiguration.
        :type: V1TLSConfiguration
        """

        self._tls_configuration = tls_configuration

    @property
    def virtual_machine_instances_per_node(self):
        """
        Gets the virtual_machine_instances_per_node of this V1KubeVirtConfiguration.

        :return: The virtual_machine_instances_per_node of this V1KubeVirtConfiguration.
        :rtype: int
        """
        return self._virtual_machine_instances_per_node

    @virtual_machine_instances_per_node.setter
    def virtual_machine_instances_per_node(self, virtual_machine_instances_per_node):
        """
        Sets the virtual_machine_instances_per_node of this V1KubeVirtConfiguration.

        :param virtual_machine_instances_per_node: The virtual_machine_instances_per_node of this V1KubeVirtConfiguration.
        :type: int
        """

        self._virtual_machine_instances_per_node = virtual_machine_instances_per_node

    @property
    def webhook_configuration(self):
        """
        Gets the webhook_configuration of this V1KubeVirtConfiguration.

        :return: The webhook_configuration of this V1KubeVirtConfiguration.
        :rtype: V1ReloadableComponentConfiguration
        """
        return self._webhook_configuration

    @webhook_configuration.setter
    def webhook_configuration(self, webhook_configuration):
        """
        Sets the webhook_configuration of this V1KubeVirtConfiguration.

        :param webhook_configuration: The webhook_configuration of this V1KubeVirtConfiguration.
        :type: V1ReloadableComponentConfiguration
        """

        self._webhook_configuration = webhook_configuration

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
        if not isinstance(other, V1KubeVirtConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
