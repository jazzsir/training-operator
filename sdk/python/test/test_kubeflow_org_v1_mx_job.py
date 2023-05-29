# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.6.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.kubeflow_org_v1_mx_job import KubeflowOrgV1MXJob  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV1MXJob(unittest.TestCase):
    """KubeflowOrgV1MXJob unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV1MXJob
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v1_mx_job.KubeflowOrgV1MXJob()  # noqa: E501
        if include_optional :
            return KubeflowOrgV1MXJob(
                api_version = '0', 
                kind = '0', 
                metadata = None, 
                spec = kubeflow_org_v1_mx_job_spec.KubeflowOrgV1MXJobSpec(
                    job_mode = '0', 
                    mx_replica_specs = {
                        'key' : kubeflow.training.models.github/com/kubeflow/common/pkg/apis/common/v1/replica_spec.github.com.kubeflow.common.pkg.apis.common.v1.ReplicaSpec(
                            replicas = 56, 
                            restart_policy = '0', 
                            template = None, )
                        }, 
                    run_policy = kubeflow.training.models.github/com/kubeflow/common/pkg/apis/common/v1/run_policy.github.com.kubeflow.common.pkg.apis.common.v1.RunPolicy(
                        active_deadline_seconds = 56, 
                        backoff_limit = 56, 
                        clean_pod_policy = '0', 
                        scheduling_policy = kubeflow.training.models.github/com/kubeflow/common/pkg/apis/common/v1/scheduling_policy.github.com.kubeflow.common.pkg.apis.common.v1.SchedulingPolicy(
                            min_available = 56, 
                            min_resources = {
                                'key' : None
                                }, 
                            priority_class = '0', 
                            queue = '0', 
                            schedule_timeout_seconds = 56, ), 
                        ttl_seconds_after_finished = 56, ), ), 
                status = kubeflow.training.models.github/com/kubeflow/common/pkg/apis/common/v1/job_status.github.com.kubeflow.common.pkg.apis.common.v1.JobStatus(
                    completion_time = None, 
                    conditions = [
                        kubeflow.training.models.github/com/kubeflow/common/pkg/apis/common/v1/job_condition.github.com.kubeflow.common.pkg.apis.common.v1.JobCondition(
                            last_transition_time = None, 
                            last_update_time = None, 
                            message = '0', 
                            reason = '0', 
                            status = '0', 
                            type = '0', )
                        ], 
                    last_reconcile_time = None, 
                    replica_statuses = {
                        'key' : kubeflow.training.models.github/com/kubeflow/common/pkg/apis/common/v1/replica_status.github.com.kubeflow.common.pkg.apis.common.v1.ReplicaStatus(
                            active = 56, 
                            failed = 56, 
                            label_selector = None, 
                            selector = '0', 
                            succeeded = 56, )
                        }, 
                    start_time = None, )
            )
        else :
            return KubeflowOrgV1MXJob(
        )

    def testKubeflowOrgV1MXJob(self):
        """Test KubeflowOrgV1MXJob"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
