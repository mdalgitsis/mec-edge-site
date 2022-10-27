# Deployment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_name** | **str** |  | 
**container_name** | **str** |  | 
**image_name** | **str** |  | 
**container_port** | **list[int]** |  | 
**container_resource_limits_cpu_value** | **str** | CPU resources are measured in milLiCPU units | [optional] 
**container_resource_limits_memory_value** | **str** | Memory is measured in bytes. | [optional] 
**container_resource_requests_cpu_value** | **str** | CPU resources are measured in milLiCPU units | [optional] 
**container_resource_requests_memory_value** | **str** | Memory is measured in bytes. | [optional] 
**pod_label** | **object** |  | 
**deployment_selector** | **object** |  | 
**deployment_label** | **object** |  | [optional] 
**replicas_number** | **int** |  | [optional] 
**env** | **list[list[object]]** |  | [optional] 
**volume_name** | **list[str]** |  | [optional] 
**container_path** | **list[str]** |  | [optional] 
**host_path** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

