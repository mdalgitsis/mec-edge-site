# swagger_client.ClusterApi

All URIs are relative to *http://localhost:8084*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_deployments**](ClusterApi.md#get_all_deployments) | **GET** /cluster/deployments | List Deployments for all Namespaces
[**get_all_limit_ranges**](ClusterApi.md#get_all_limit_ranges) | **GET** /cluster/limitranges | List LimitRanges for all Namespaces
[**get_all_pods**](ClusterApi.md#get_all_pods) | **GET** /cluster/pods | List Pods for all Namespaces
[**get_all_resource_quotas**](ClusterApi.md#get_all_resource_quotas) | **GET** /cluster/resourcequotas | List ResourceQuotas for all Namespaces
[**get_all_service_monitors**](ClusterApi.md#get_all_service_monitors) | **GET** /cluster/servicemonitors | List ServiceMonitors for all Namespaces
[**get_all_services**](ClusterApi.md#get_all_services) | **GET** /cluster/services | List Services for all Namespaces
[**get_node_status**](ClusterApi.md#get_node_status) | **GET** /cluster/nodes/{node_name}/status | Get a specific Node
[**get_nodes**](ClusterApi.md#get_nodes) | **GET** /cluster/nodes | List the existing Nodes of the cluster

# **get_all_deployments**
> get_all_deployments()

List Deployments for all Namespaces

Returns a list of all Deployment names of the Kubernetes cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # List Deployments for all Namespaces
    api_instance.get_all_deployments()
except ApiException as e:
    print("Exception when calling ClusterApi->get_all_deployments: %s\n" % e)
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

# **get_all_limit_ranges**
> get_all_limit_ranges()

List LimitRanges for all Namespaces

Returns a list of all LimitRanges of the Kubernetes cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # List LimitRanges for all Namespaces
    api_instance.get_all_limit_ranges()
except ApiException as e:
    print("Exception when calling ClusterApi->get_all_limit_ranges: %s\n" % e)
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

# **get_all_pods**
> get_all_pods()

List Pods for all Namespaces

Returns a list of all Pods of the Kubernetes cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # List Pods for all Namespaces
    api_instance.get_all_pods()
except ApiException as e:
    print("Exception when calling ClusterApi->get_all_pods: %s\n" % e)
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

# **get_all_resource_quotas**
> get_all_resource_quotas()

List ResourceQuotas for all Namespaces

Returns a list of all ResourceQuotas of the Kubernetes cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # List ResourceQuotas for all Namespaces
    api_instance.get_all_resource_quotas()
except ApiException as e:
    print("Exception when calling ClusterApi->get_all_resource_quotas: %s\n" % e)
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

# **get_all_service_monitors**
> get_all_service_monitors()

List ServiceMonitors for all Namespaces

Returns a list of all ServiceMonitors of the Kubernetes cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # List ServiceMonitors for all Namespaces
    api_instance.get_all_service_monitors()
except ApiException as e:
    print("Exception when calling ClusterApi->get_all_service_monitors: %s\n" % e)
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

# **get_all_services**
> get_all_services()

List Services for all Namespaces

Returns a list of all Services of the Kubernetes cluster

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # List Services for all Namespaces
    api_instance.get_all_services()
except ApiException as e:
    print("Exception when calling ClusterApi->get_all_services: %s\n" % e)
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

# **get_node_status**
> get_node_status(node_name)

Get a specific Node

Returns the status and the IP information of the Node

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()
node_name = 'node_name_example' # str | name of Node

try:
    # Get a specific Node
    api_instance.get_node_status(node_name)
except ApiException as e:
    print("Exception when calling ClusterApi->get_node_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_name** | **str**| name of Node | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes**
> get_nodes()

List the existing Nodes of the cluster

Returns a list of all cluster Nodes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClusterApi()

try:
    # List the existing Nodes of the cluster
    api_instance.get_nodes()
except ApiException as e:
    print("Exception when calling ClusterApi->get_nodes: %s\n" % e)
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

