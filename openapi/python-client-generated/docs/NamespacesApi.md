# swagger_client.NamespacesApi

All URIs are relative to *http://localhost:8084*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_namespace**](NamespacesApi.md#add_namespace) | **POST** /namespaces | Create a Namespace
[**add_namespaced_deployment**](NamespacesApi.md#add_namespaced_deployment) | **POST** /namespaces/{namespace_name}/deployments | Create a Deployment in a specific namespace
[**add_namespaced_limit_range**](NamespacesApi.md#add_namespaced_limit_range) | **POST** /namespaces/{namespace_name}/limitranges | Create a LimitRange in a specific namespace
[**add_namespaced_pod**](NamespacesApi.md#add_namespaced_pod) | **POST** /namespaces/{namespace_name}/pods | Create a Pod in a Namespace
[**add_namespaced_resource_quota**](NamespacesApi.md#add_namespaced_resource_quota) | **POST** /namespaces/{namespace_name}/resourcequotas | Create a ResourceQuota in a specific namespace
[**add_namespaced_service**](NamespacesApi.md#add_namespaced_service) | **POST** /namespaces/{namespace_name}/services | Create a Service in a specific namespace
[**add_namespaced_service_monitor**](NamespacesApi.md#add_namespaced_service_monitor) | **POST** /namespaces/{namespace_name}/servicemonitors | Create a ServiceMonitor in a specific namespace
[**delete_namespace**](NamespacesApi.md#delete_namespace) | **DELETE** /namespaces/{namespace_name} | Delete a Namespace
[**delete_namespaced_deployment**](NamespacesApi.md#delete_namespaced_deployment) | **DELETE** /namespaces/{namespace_name}/deployments/{deployment_name} | Delete a namespaced Deployment
[**delete_namespaced_limit_range**](NamespacesApi.md#delete_namespaced_limit_range) | **DELETE** /namespaces/{namespace_name}/limitranges/{limitrange_name} | Delete a namespaced LimitRange
[**delete_namespaced_pod**](NamespacesApi.md#delete_namespaced_pod) | **DELETE** /namespaces/{namespace_name}/pods/{pod_name} | Delete a Pod from a specific Namespace
[**delete_namespaced_resource_quota**](NamespacesApi.md#delete_namespaced_resource_quota) | **DELETE** /namespaces/{namespace_name}/resourcequotas/{resourcequota_name} | Delete a namespaced ResourceQuota
[**delete_namespaced_service**](NamespacesApi.md#delete_namespaced_service) | **DELETE** /namespaces/{namespace_name}/services/{service_name} | Delete a namespaced Service
[**delete_namespaced_service_monitor**](NamespacesApi.md#delete_namespaced_service_monitor) | **DELETE** /namespaces/{namespace_name}/servicemonitors/{servicemonitor_name} | Delete a namespaced ServiceMonitor
[**get_namespaced_deployment**](NamespacesApi.md#get_namespaced_deployment) | **GET** /namespaces/{namespace_name}/deployments/{deployment_name} | Read a namespaced Deployment definition
[**get_namespaced_deployment_resources**](NamespacesApi.md#get_namespaced_deployment_resources) | **GET** /namespaces/{namespace_name}/deployments/{deployment_name}/resources | Read namespaced Deployment resources
[**get_namespaced_deployment_scale_replicas**](NamespacesApi.md#get_namespaced_deployment_scale_replicas) | **GET** /namespaces/{namespace_name}/deployments/{deployment_name}/replicas | Read namespaced Deployment Scale replicas
[**get_namespaced_deployment_status**](NamespacesApi.md#get_namespaced_deployment_status) | **GET** /namespaces/{namespace_name}/deployments/{deployment_name}/status | Read namespaced Deployment status
[**get_namespaced_deployments**](NamespacesApi.md#get_namespaced_deployments) | **GET** /namespaces/{namespace_name}/deployments | List Deployments of a specific Namespace
[**get_namespaced_limit_range**](NamespacesApi.md#get_namespaced_limit_range) | **GET** /namespaces/{namespace_name}/limitranges/{limitrange_name} | Read a namespaced LimitRange definition
[**get_namespaced_limit_ranges**](NamespacesApi.md#get_namespaced_limit_ranges) | **GET** /namespaces/{namespace_name}/limitranges | List LimitRanges by namespace
[**get_namespaced_pod_logs**](NamespacesApi.md#get_namespaced_pod_logs) | **GET** /namespaces/{namespace_name}/pods/{pod_name}/logs | Get logs of a namespaced Pod
[**get_namespaced_pods**](NamespacesApi.md#get_namespaced_pods) | **GET** /namespaces/{namespace_name}/pods | List Pods by Namespace
[**get_namespaced_resource_quota**](NamespacesApi.md#get_namespaced_resource_quota) | **GET** /namespaces/{namespace_name}/resourcequotas/{resourcequota_name} | Read a namespaced ResourceQuota definition
[**get_namespaced_resource_quotas**](NamespacesApi.md#get_namespaced_resource_quotas) | **GET** /namespaces/{namespace_name}/resourcequotas | List ResourceQuotas by namespace
[**get_namespaced_service**](NamespacesApi.md#get_namespaced_service) | **GET** /namespaces/{namespace_name}/services/{service_name} | Read a namespaced Service definition
[**get_namespaced_service_monitor**](NamespacesApi.md#get_namespaced_service_monitor) | **GET** /namespaces/{namespace_name}/servicemonitors/{servicemonitor_name} | Read a namespaced ServiceMonitor definition
[**get_namespaced_service_monitors**](NamespacesApi.md#get_namespaced_service_monitors) | **GET** /namespaces/{namespace_name}/servicemonitors | List ServiceMonitors by namespace
[**get_namespaced_service_status**](NamespacesApi.md#get_namespaced_service_status) | **GET** /namespaces/{namespace_name}/services/{service_name}/status | Read namespaced Service status
[**get_namespaced_services**](NamespacesApi.md#get_namespaced_services) | **GET** /namespaces/{namespace_name}/services | List Services by namespace
[**get_namespaces**](NamespacesApi.md#get_namespaces) | **GET** /namespaces | List all Namespaces
[**scale_horizontal_namespaced_deployment**](NamespacesApi.md#scale_horizontal_namespaced_deployment) | **PUT** /namespaces/{namespace_name}/deployments/{deployment_name}/scaleHorizontal | Scale Horizontal a namespaced Deployment
[**scale_vertical_namespaced_deployment**](NamespacesApi.md#scale_vertical_namespaced_deployment) | **PATCH** /namespaces/{namespace_name}/deployments/{deployment_name}/{container_name}/scaleVertical | Scale Vertical a namespaced Deployment

# **add_namespace**
> add_namespace(body)

Create a Namespace

Create a Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.Namespace() # Namespace | Namespace object that contains the name to create a Namespace

try:
    # Create a Namespace
    api_instance.add_namespace(body)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Namespace**](Namespace.md)| Namespace object that contains the name to create a Namespace | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_namespaced_deployment**
> add_namespaced_deployment(body, namespace_name)

Create a Deployment in a specific namespace

Create a namespaced Deployment Kubernetes-resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.Deployment() # Deployment | Deployment object that needs to be added to create a Deployment-resource in the cluster. **Note:** If you specify a limit for a resource, but do not specify any request, then Kubernetes copies the limit you specified and uses it as the requested value for the resource.  Also, replicas_number must be >= 1 and deployment_name must contain only lowercase alphanumeric characters or '-'.
namespace_name = 'namespace_name_example' # str | name of Namespace to create a Deployment

try:
    # Create a Deployment in a specific namespace
    api_instance.add_namespaced_deployment(body, namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Deployment**](Deployment.md)| Deployment object that needs to be added to create a Deployment-resource in the cluster. **Note:** If you specify a limit for a resource, but do not specify any request, then Kubernetes copies the limit you specified and uses it as the requested value for the resource.  Also, replicas_number must be &gt;&#x3D; 1 and deployment_name must contain only lowercase alphanumeric characters or &#x27;-&#x27;. | 
 **namespace_name** | **str**| name of Namespace to create a Deployment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_namespaced_limit_range**
> add_namespaced_limit_range(body, namespace_name)

Create a LimitRange in a specific namespace

Create a namespaced LimitRange Kubernetes-resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.LimitRange() # LimitRange | LimitRanges pose default cpu and memory resource reservation in the specified namespaces.
namespace_name = 'namespace_name_example' # str | name of namespace to create a LimitRange

try:
    # Create a LimitRange in a specific namespace
    api_instance.add_namespaced_limit_range(body, namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespaced_limit_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LimitRange**](LimitRange.md)| LimitRanges pose default cpu and memory resource reservation in the specified namespaces. | 
 **namespace_name** | **str**| name of namespace to create a LimitRange | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_namespaced_pod**
> add_namespaced_pod(body, namespace_name)

Create a Pod in a Namespace

Create a Pod in a specific Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.Pod() # Pod | Pod object that contains the key-value pairs to create a pod. **Note:** pod_name for good practices should contain only lowercase alphanumeric characters with or without '-'
namespace_name = 'namespace_name_example' # str | name of Namespace to create a Pod

try:
    # Create a Pod in a Namespace
    api_instance.add_namespaced_pod(body, namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespaced_pod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pod**](Pod.md)| Pod object that contains the key-value pairs to create a pod. **Note:** pod_name for good practices should contain only lowercase alphanumeric characters with or without &#x27;-&#x27; | 
 **namespace_name** | **str**| name of Namespace to create a Pod | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_namespaced_resource_quota**
> add_namespaced_resource_quota(body, namespace_name)

Create a ResourceQuota in a specific namespace

Create a namespaced ResourceQuota Kubernetes-resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.ResourceQuota() # ResourceQuota | Resourcequotas reserve cpu,memory and storage resources in the specified namespaces.
namespace_name = 'namespace_name_example' # str | name of namespace to create a ResourceQuota

try:
    # Create a ResourceQuota in a specific namespace
    api_instance.add_namespaced_resource_quota(body, namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespaced_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResourceQuota**](ResourceQuota.md)| Resourcequotas reserve cpu,memory and storage resources in the specified namespaces. | 
 **namespace_name** | **str**| name of namespace to create a ResourceQuota | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_namespaced_service**
> add_namespaced_service(body, namespace_name)

Create a Service in a specific namespace

Create a namespaced Service Kubernetes-resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.Service() # Service | Service object that needs to be added to expose Pod-resources in or out the cluster. **Note:** service_name must contain only lowercase alphanumeric characters or '-'.  The Service selector should match the label of the pod. The Service targetPort should match the container_port of the container inside the Pod. If service_type is ClusterIP, nodePort value must be set null in the service_port variable. Finally port_name is also optional.
namespace_name = 'namespace_name_example' # str | name of namespace to create a Service

try:
    # Create a Service in a specific namespace
    api_instance.add_namespaced_service(body, namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespaced_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Service**](Service.md)| Service object that needs to be added to expose Pod-resources in or out the cluster. **Note:** service_name must contain only lowercase alphanumeric characters or &#x27;-&#x27;.  The Service selector should match the label of the pod. The Service targetPort should match the container_port of the container inside the Pod. If service_type is ClusterIP, nodePort value must be set null in the service_port variable. Finally port_name is also optional. | 
 **namespace_name** | **str**| name of namespace to create a Service | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_namespaced_service_monitor**
> add_namespaced_service_monitor(body, namespace_name)

Create a ServiceMonitor in a specific namespace

Create a namespaced ServiceMonitor Custom Kubernetes-resource

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.ServiceMonitor() # ServiceMonitor | ServiceMonitor Custom object that needs to be added to expose Pod-resources in the Prometheus server. **Note:** service_name must contain only lowercase alphanumeric characters or '-'.  The Service selector should match the label of the pod. The endpoints should match the Service port names. A release label must exist wit the value of the Prometheus name. If Prometheus is installed by a helm chart, the release value is the helm release name.
namespace_name = 'namespace_name_example' # str | name of namespace to create a ServiceMonitor

try:
    # Create a ServiceMonitor in a specific namespace
    api_instance.add_namespaced_service_monitor(body, namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->add_namespaced_service_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ServiceMonitor**](ServiceMonitor.md)| ServiceMonitor Custom object that needs to be added to expose Pod-resources in the Prometheus server. **Note:** service_name must contain only lowercase alphanumeric characters or &#x27;-&#x27;.  The Service selector should match the label of the pod. The endpoints should match the Service port names. A release label must exist wit the value of the Prometheus name. If Prometheus is installed by a helm chart, the release value is the helm release name. | 
 **namespace_name** | **str**| name of namespace to create a ServiceMonitor | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespace**
> delete_namespace(namespace_name)

Delete a Namespace

Delete a Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of Namespace to delete

try:
    # Delete a Namespace
    api_instance.delete_namespace(namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of Namespace to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_deployment**
> delete_namespaced_deployment(namespace_name, deployment_name)

Delete a namespaced Deployment

Delete a namespaced Deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the Deployment lives
deployment_name = 'deployment_name_example' # str | name of Deployment to delete

try:
    # Delete a namespaced Deployment
    api_instance.delete_namespaced_deployment(namespace_name, deployment_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the Deployment lives | 
 **deployment_name** | **str**| name of Deployment to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_limit_range**
> delete_namespaced_limit_range(namespace_name, limitrange_name)

Delete a namespaced LimitRange

Delete a namespaced LimitRange

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the LimitRange lives
limitrange_name = 'limitrange_name_example' # str | name of LimitRange to delete

try:
    # Delete a namespaced LimitRange
    api_instance.delete_namespaced_limit_range(namespace_name, limitrange_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespaced_limit_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the LimitRange lives | 
 **limitrange_name** | **str**| name of LimitRange to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_pod**
> delete_namespaced_pod(namespace_name, pod_name)

Delete a Pod from a specific Namespace

Delete a namespaced Pod

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of Namespace where the Pod lives
pod_name = 'pod_name_example' # str | name of Pod to delete

try:
    # Delete a Pod from a specific Namespace
    api_instance.delete_namespaced_pod(namespace_name, pod_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespaced_pod: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of Namespace where the Pod lives | 
 **pod_name** | **str**| name of Pod to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_resource_quota**
> delete_namespaced_resource_quota(namespace_name, resourcequota_name)

Delete a namespaced ResourceQuota

Delete a namespaced ResourceQuota

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the ResourceQuota lives
resourcequota_name = 'resourcequota_name_example' # str | name of ResourceQuota to delete

try:
    # Delete a namespaced ResourceQuota
    api_instance.delete_namespaced_resource_quota(namespace_name, resourcequota_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespaced_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the ResourceQuota lives | 
 **resourcequota_name** | **str**| name of ResourceQuota to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_service**
> delete_namespaced_service(namespace_name, service_name)

Delete a namespaced Service

Delete a namespaced Service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the Service lives
service_name = 'service_name_example' # str | name of Service to delete

try:
    # Delete a namespaced Service
    api_instance.delete_namespaced_service(namespace_name, service_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespaced_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the Service lives | 
 **service_name** | **str**| name of Service to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_namespaced_service_monitor**
> delete_namespaced_service_monitor(namespace_name, servicemonitor_name)

Delete a namespaced ServiceMonitor

Delete a namespaced ServiceMonitor

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the ServiceMonitor lives
servicemonitor_name = 'servicemonitor_name_example' # str | name of ServiceMonitor to delete

try:
    # Delete a namespaced ServiceMonitor
    api_instance.delete_namespaced_service_monitor(namespace_name, servicemonitor_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->delete_namespaced_service_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the ServiceMonitor lives | 
 **servicemonitor_name** | **str**| name of ServiceMonitor to delete | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_deployment**
> get_namespaced_deployment(namespace_name, deployment_name)

Read a namespaced Deployment definition

Returns the definition of a single Deployment by deployment_name in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of Namespace where the Deployment lives
deployment_name = 'deployment_name_example' # str | name of Deployment to retrieve

try:
    # Read a namespaced Deployment definition
    api_instance.get_namespaced_deployment(namespace_name, deployment_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of Namespace where the Deployment lives | 
 **deployment_name** | **str**| name of Deployment to retrieve | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_deployment_resources**
> get_namespaced_deployment_resources(namespace_name, deployment_name)

Read namespaced Deployment resources

Read resources in terms of CPU and memory of the specified Deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the Deployment lives
deployment_name = 'deployment_name_example' # str | name of Deployment to show the resources

try:
    # Read namespaced Deployment resources
    api_instance.get_namespaced_deployment_resources(namespace_name, deployment_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_deployment_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the Deployment lives | 
 **deployment_name** | **str**| name of Deployment to show the resources | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_deployment_scale_replicas**
> get_namespaced_deployment_scale_replicas(namespace_name, deployment_name)

Read namespaced Deployment Scale replicas

Read replicas of the Scale definition of the specified Deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the Deployment lives
deployment_name = 'deployment_name_example' # str | name of Deployment to show the number of replicas

try:
    # Read namespaced Deployment Scale replicas
    api_instance.get_namespaced_deployment_scale_replicas(namespace_name, deployment_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_deployment_scale_replicas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the Deployment lives | 
 **deployment_name** | **str**| name of Deployment to show the number of replicas | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_deployment_status**
> get_namespaced_deployment_status(namespace_name, deployment_name)

Read namespaced Deployment status

Read status of the specified Deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the Deployment lives
deployment_name = 'deployment_name_example' # str | name of Deployment to show its status

try:
    # Read namespaced Deployment status
    api_instance.get_namespaced_deployment_status(namespace_name, deployment_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_deployment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the Deployment lives | 
 **deployment_name** | **str**| name of Deployment to show its status | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_deployments**
> get_namespaced_deployments(namespace_name)

List Deployments of a specific Namespace

Returns a list with the names of the Deployments of a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of Namespace to retrieve the Deployment-resources

try:
    # List Deployments of a specific Namespace
    api_instance.get_namespaced_deployments(namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_deployments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of Namespace to retrieve the Deployment-resources | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_limit_range**
> get_namespaced_limit_range(namespace_name, limitrange_name)

Read a namespaced LimitRange definition

Returns the definition of a single LimitRange by limitrange_name in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the LimitRange lives
limitrange_name = 'limitrange_name_example' # str | name of LimitRange to retrieve

try:
    # Read a namespaced LimitRange definition
    api_instance.get_namespaced_limit_range(namespace_name, limitrange_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_limit_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the LimitRange lives | 
 **limitrange_name** | **str**| name of LimitRange to retrieve | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_limit_ranges**
> get_namespaced_limit_ranges(namespace_name)

List LimitRanges by namespace

Returns a list with all the LimitRanges in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace to retrieve the LimitRanges

try:
    # List LimitRanges by namespace
    api_instance.get_namespaced_limit_ranges(namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_limit_ranges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace to retrieve the LimitRanges | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_pod_logs**
> get_namespaced_pod_logs(namespace_name, pod_name)

Get logs of a namespaced Pod

Get logs of a namespaced Pod

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of Namespace where the pod lives
pod_name = 'pod_name_example' # str | name of Pod to return the logs

try:
    # Get logs of a namespaced Pod
    api_instance.get_namespaced_pod_logs(namespace_name, pod_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_pod_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of Namespace where the pod lives | 
 **pod_name** | **str**| name of Pod to return the logs | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_pods**
> get_namespaced_pods(namespace_name)

List Pods by Namespace

Returns a list with all the Pods in a specific Namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of Namespace to retrieve the Pods

try:
    # List Pods by Namespace
    api_instance.get_namespaced_pods(namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_pods: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of Namespace to retrieve the Pods | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_resource_quota**
> get_namespaced_resource_quota(namespace_name, resourcequota_name)

Read a namespaced ResourceQuota definition

Returns the definition of a single ResourceQuota by resourcequota_name in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the ResourceQuota lives
resourcequota_name = 'resourcequota_name_example' # str | name of ResourceQuota to retrieve

try:
    # Read a namespaced ResourceQuota definition
    api_instance.get_namespaced_resource_quota(namespace_name, resourcequota_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_resource_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the ResourceQuota lives | 
 **resourcequota_name** | **str**| name of ResourceQuota to retrieve | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_resource_quotas**
> get_namespaced_resource_quotas(namespace_name)

List ResourceQuotas by namespace

Returns a list with all the ResourceQuotas in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace to retrieve the ResourceQuotas

try:
    # List ResourceQuotas by namespace
    api_instance.get_namespaced_resource_quotas(namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_resource_quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace to retrieve the ResourceQuotas | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_service**
> get_namespaced_service(namespace_name, service_name)

Read a namespaced Service definition

Returns the definition of a single Service by service_name in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the Service lives
service_name = 'service_name_example' # str | name of Service to retrieve

try:
    # Read a namespaced Service definition
    api_instance.get_namespaced_service(namespace_name, service_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_service: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the Service lives | 
 **service_name** | **str**| name of Service to retrieve | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_service_monitor**
> get_namespaced_service_monitor(namespace_name, servicemonitor_name)

Read a namespaced ServiceMonitor definition

Returns the definition of a single ServiceMonitor by servicemonitor_name in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the ServiceMonitor lives
servicemonitor_name = 'servicemonitor_name_example' # str | name of ServiceMonitor to retrieve

try:
    # Read a namespaced ServiceMonitor definition
    api_instance.get_namespaced_service_monitor(namespace_name, servicemonitor_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_service_monitor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the ServiceMonitor lives | 
 **servicemonitor_name** | **str**| name of ServiceMonitor to retrieve | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_service_monitors**
> get_namespaced_service_monitors(namespace_name)

List ServiceMonitors by namespace

Returns a list with all the ServiceMonitors in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace to retrieve the ServiceMonitors

try:
    # List ServiceMonitors by namespace
    api_instance.get_namespaced_service_monitors(namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_service_monitors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace to retrieve the ServiceMonitors | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_service_status**
> get_namespaced_service_status(namespace_name, service_name)

Read namespaced Service status

Read the status of the specified Service, like the Internal service IP, the External Service IP, the service ports and the service type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace where the Service lives
service_name = 'service_name_example' # str | name of Service to show its status

try:
    # Read namespaced Service status
    api_instance.get_namespaced_service_status(namespace_name, service_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_service_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace where the Service lives | 
 **service_name** | **str**| name of Service to show its status | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaced_services**
> get_namespaced_services(namespace_name)

List Services by namespace

Returns a list with all the Services in a specific namespace

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
namespace_name = 'namespace_name_example' # str | name of namespace to retrieve the Services

try:
    # List Services by namespace
    api_instance.get_namespaced_services(namespace_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaced_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **namespace_name** | **str**| name of namespace to retrieve the Services | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_namespaces**
> get_namespaces()

List all Namespaces

Returns a list of all Namespaces in the cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()

try:
    # List all Namespaces
    api_instance.get_namespaces()
except ApiException as e:
    print("Exception when calling NamespacesApi->get_namespaces: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scale_horizontal_namespaced_deployment**
> scale_horizontal_namespaced_deployment(body, namespace_name, deployment_name)

Scale Horizontal a namespaced Deployment

Scale either up or down the pods of a namespaced Deployment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.ScaleHorizontal() # ScaleHorizontal | Scale Horizontal object that needs to be added to a namespaced Deployment in order to scale up or down the pods (containers) it contains. **Note:** if replicas_number = 0, then we kill all the pods of the Deployment.
namespace_name = 'namespace_name_example' # str | name of namespace where the Deployment lives
deployment_name = 'deployment_name_example' # str | name of Deployment to scale horizontically

try:
    # Scale Horizontal a namespaced Deployment
    api_instance.scale_horizontal_namespaced_deployment(body, namespace_name, deployment_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->scale_horizontal_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScaleHorizontal**](ScaleHorizontal.md)| Scale Horizontal object that needs to be added to a namespaced Deployment in order to scale up or down the pods (containers) it contains. **Note:** if replicas_number &#x3D; 0, then we kill all the pods of the Deployment. | 
 **namespace_name** | **str**| name of namespace where the Deployment lives | 
 **deployment_name** | **str**| name of Deployment to scale horizontically | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scale_vertical_namespaced_deployment**
> scale_vertical_namespaced_deployment(body, namespace_name, deployment_name, container_name)

Scale Vertical a namespaced Deployment

Partialy update a namespaced Deployment - Vertical scaling. The update affects the pod-container resources such as CPU and memory.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NamespacesApi()
body = swagger_client.ScaleVertical() # ScaleVertical | ScaleVertical object that needs to be added to a namespaced Deployment in the cluster to perform vertical scaling. **Note:** If you specify a limit for a resource, but do not specify any request, then Kubernetes copies the limit you specified and uses it as the requested value for the resource.
namespace_name = 'namespace_name_example' # str | name of namespace where the Deployment lives
deployment_name = 'deployment_name_example' # str | name of Deployment to scale vertically
container_name = 'container_name_example' # str | name of container of the Deployment to scale vertically

try:
    # Scale Vertical a namespaced Deployment
    api_instance.scale_vertical_namespaced_deployment(body, namespace_name, deployment_name, container_name)
except ApiException as e:
    print("Exception when calling NamespacesApi->scale_vertical_namespaced_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScaleVertical**](ScaleVertical.md)| ScaleVertical object that needs to be added to a namespaced Deployment in the cluster to perform vertical scaling. **Note:** If you specify a limit for a resource, but do not specify any request, then Kubernetes copies the limit you specified and uses it as the requested value for the resource. | 
 **namespace_name** | **str**| name of namespace where the Deployment lives | 
 **deployment_name** | **str**| name of Deployment to scale vertically | 
 **container_name** | **str**| name of container of the Deployment to scale vertically | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

