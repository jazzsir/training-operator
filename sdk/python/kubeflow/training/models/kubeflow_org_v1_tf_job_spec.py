# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class KubeflowOrgV1TFJobSpec(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'enable_dynamic_worker': 'bool',
        'run_policy': 'GithubComKubeflowCommonPkgApisCommonV1RunPolicy',
        'success_policy': 'str',
        'tf_replica_specs': 'dict(str, GithubComKubeflowCommonPkgApisCommonV1ReplicaSpec)'
    }

    attribute_map = {
        'enable_dynamic_worker': 'enableDynamicWorker',
        'run_policy': 'runPolicy',
        'success_policy': 'successPolicy',
        'tf_replica_specs': 'tfReplicaSpecs'
    }

    def __init__(self, enable_dynamic_worker=None, run_policy=None, success_policy=None, tf_replica_specs=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV1TFJobSpec - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._enable_dynamic_worker = None
        self._run_policy = None
        self._success_policy = None
        self._tf_replica_specs = None
        self.discriminator = None

        if enable_dynamic_worker is not None:
            self.enable_dynamic_worker = enable_dynamic_worker
        self.run_policy = run_policy
        if success_policy is not None:
            self.success_policy = success_policy
        self.tf_replica_specs = tf_replica_specs

    @property
    def enable_dynamic_worker(self):
        """Gets the enable_dynamic_worker of this KubeflowOrgV1TFJobSpec.  # noqa: E501

        A switch to enable dynamic worker  # noqa: E501

        :return: The enable_dynamic_worker of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :rtype: bool
        """
        return self._enable_dynamic_worker

    @enable_dynamic_worker.setter
    def enable_dynamic_worker(self, enable_dynamic_worker):
        """Sets the enable_dynamic_worker of this KubeflowOrgV1TFJobSpec.

        A switch to enable dynamic worker  # noqa: E501

        :param enable_dynamic_worker: The enable_dynamic_worker of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :type: bool
        """

        self._enable_dynamic_worker = enable_dynamic_worker

    @property
    def run_policy(self):
        """Gets the run_policy of this KubeflowOrgV1TFJobSpec.  # noqa: E501


        :return: The run_policy of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :rtype: GithubComKubeflowCommonPkgApisCommonV1RunPolicy
        """
        return self._run_policy

    @run_policy.setter
    def run_policy(self, run_policy):
        """Sets the run_policy of this KubeflowOrgV1TFJobSpec.


        :param run_policy: The run_policy of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :type: GithubComKubeflowCommonPkgApisCommonV1RunPolicy
        """
        if self.local_vars_configuration.client_side_validation and run_policy is None:  # noqa: E501
            raise ValueError("Invalid value for `run_policy`, must not be `None`")  # noqa: E501

        self._run_policy = run_policy

    @property
    def success_policy(self):
        """Gets the success_policy of this KubeflowOrgV1TFJobSpec.  # noqa: E501

        SuccessPolicy defines the policy to mark the TFJob as succeeded. Default to \"\", using the default rules.  # noqa: E501

        :return: The success_policy of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :rtype: str
        """
        return self._success_policy

    @success_policy.setter
    def success_policy(self, success_policy):
        """Sets the success_policy of this KubeflowOrgV1TFJobSpec.

        SuccessPolicy defines the policy to mark the TFJob as succeeded. Default to \"\", using the default rules.  # noqa: E501

        :param success_policy: The success_policy of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :type: str
        """

        self._success_policy = success_policy

    @property
    def tf_replica_specs(self):
        """Gets the tf_replica_specs of this KubeflowOrgV1TFJobSpec.  # noqa: E501

        A map of TFReplicaType (type) to ReplicaSpec (value). Specifies the TF cluster configuration. For example,   {     \"PS\": ReplicaSpec,     \"Worker\": ReplicaSpec,   }  # noqa: E501

        :return: The tf_replica_specs of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :rtype: dict(str, GithubComKubeflowCommonPkgApisCommonV1ReplicaSpec)
        """
        return self._tf_replica_specs

    @tf_replica_specs.setter
    def tf_replica_specs(self, tf_replica_specs):
        """Sets the tf_replica_specs of this KubeflowOrgV1TFJobSpec.

        A map of TFReplicaType (type) to ReplicaSpec (value). Specifies the TF cluster configuration. For example,   {     \"PS\": ReplicaSpec,     \"Worker\": ReplicaSpec,   }  # noqa: E501

        :param tf_replica_specs: The tf_replica_specs of this KubeflowOrgV1TFJobSpec.  # noqa: E501
        :type: dict(str, GithubComKubeflowCommonPkgApisCommonV1ReplicaSpec)
        """
        if self.local_vars_configuration.client_side_validation and tf_replica_specs is None:  # noqa: E501
            raise ValueError("Invalid value for `tf_replica_specs`, must not be `None`")  # noqa: E501

        self._tf_replica_specs = tf_replica_specs

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubeflowOrgV1TFJobSpec):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV1TFJobSpec):
            return True

        return self.to_dict() != other.to_dict()
