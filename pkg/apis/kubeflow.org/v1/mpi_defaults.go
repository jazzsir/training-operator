// Copyright 2019 The Kubeflow Authors.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package v1

import (
	"k8s.io/apimachinery/pkg/runtime"

	commonv1 "github.com/jazzsir/common/pkg/apis/common/v1"
)

func addMPIJobDefaultingFuncs(scheme *runtime.Scheme) error {
	return RegisterDefaults(scheme)
}

func SetDefaults_MPIJob(mpiJob *MPIJob) {
	// Set default CleanPodPolicy to None when neither fields specified.
	if mpiJob.Spec.CleanPodPolicy == nil && mpiJob.Spec.RunPolicy.CleanPodPolicy == nil {
		none := commonv1.CleanPodPolicyNone
		mpiJob.Spec.CleanPodPolicy = &none
		mpiJob.Spec.RunPolicy.CleanPodPolicy = &none
	}

	// Set default replicas
	setDefaultReplicas(mpiJob.Spec.MPIReplicaSpecs[MPIJobReplicaTypeLauncher], 1)
	setDefaultReplicas(mpiJob.Spec.MPIReplicaSpecs[MPIJobReplicaTypeWorker], 0)

	// Set default restartPolicy
	setDefaultRestartPolicy(mpiJob.Spec.MPIReplicaSpecs[MPIJobReplicaTypeLauncher], MPIJobDefaultRestartPolicy)
	setDefaultRestartPolicy(mpiJob.Spec.MPIReplicaSpecs[MPIJobReplicaTypeWorker], MPIJobDefaultRestartPolicy)
}
