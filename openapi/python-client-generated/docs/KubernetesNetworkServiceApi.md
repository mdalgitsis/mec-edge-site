# swagger_client.KubernetesNetworkServiceApi

All URIs are relative to *http://localhost:8084*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kns**](KubernetesNetworkServiceApi.md#add_kns) | **POST** /kns | Create a Kubernetes Network Service
[**delete_kns**](KubernetesNetworkServiceApi.md#delete_kns) | **DELETE** /kns/{kns_name} | Delete a Kubernetes Network Service
[**get_all_kns**](KubernetesNetworkServiceApi.md#get_all_kns) | **GET** /kns | List Kubernetes Network Services
[**get_kns**](KubernetesNetworkServiceApi.md#get_kns) | **GET** /kns/{kns_name} | Get a Kubernetes Network Service
[**update_kns**](KubernetesNetworkServiceApi.md#update_kns) | **POST** /kns/{kns_name}/day2actions | Day2Actions in a Kubernetes Network Service

# **add_kns**
> add_kns(body)

Create a Kubernetes Network Service

Create a KNS in OSM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KubernetesNetworkServiceApi()
body = swagger_client.KNS() # KNS | Body request that contains the key-value pairs to create a KNS. **Note:** a note comes here

try:
    # Create a Kubernetes Network Service
    api_instance.add_kns(body)
except ApiException as e:
    print("Exception when calling KubernetesNetworkServiceApi->add_kns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KNS**](KNS.md)| Body request that contains the key-value pairs to create a KNS. **Note:** a note comes here | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kns**
> delete_kns(kns_name)

Delete a Kubernetes Network Service

Delete a KNS in OSM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KubernetesNetworkServiceApi()
kns_name = 'kns_name_example' # str | Name of the KNS

try:
    # Delete a Kubernetes Network Service
    api_instance.delete_kns(kns_name)
except ApiException as e:
    print("Exception when calling KubernetesNetworkServiceApi->delete_kns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kns_name** | **str**| Name of the KNS | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_kns**
> get_all_kns()

List Kubernetes Network Services

Returns a list with all the KNS running in OSM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KubernetesNetworkServiceApi()

try:
    # List Kubernetes Network Services
    api_instance.get_all_kns()
except ApiException as e:
    print("Exception when calling KubernetesNetworkServiceApi->get_all_kns: %s\n" % e)
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

# **get_kns**
> get_kns(kns_name)

Get a Kubernetes Network Service

Returns a KNS running in OSM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KubernetesNetworkServiceApi()
kns_name = 'kns_name_example' # str | Name of the KNS

try:
    # Get a Kubernetes Network Service
    api_instance.get_kns(kns_name)
except ApiException as e:
    print("Exception when calling KubernetesNetworkServiceApi->get_kns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kns_name** | **str**| Name of the KNS | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kns**
> update_kns(body, nsd_name, vim_name, k8s_namespace, kns_name)

Day2Actions in a Kubernetes Network Service

Performs Day2Actions in a KNS in OSM

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.KubernetesNetworkServiceApi()
body = swagger_client.KNSDay2Actions() # KNSDay2Actions | Body request that contains the key-value pairs to update a KNS. **Note:** a note comes here
nsd_name = 'nsd_name_example' # str | Name of the ND Descriptor
vim_name = 'vim_name_example' # str | Name of the VIM
k8s_namespace = 'k8s_namespace_example' # str | Name of the Namespace in Kubernetes (K8s)
kns_name = 'kns_name_example' # str | Name of the KNS

try:
    # Day2Actions in a Kubernetes Network Service
    api_instance.update_kns(body, nsd_name, vim_name, k8s_namespace, kns_name)
except ApiException as e:
    print("Exception when calling KubernetesNetworkServiceApi->update_kns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KNSDay2Actions**](KNSDay2Actions.md)| Body request that contains the key-value pairs to update a KNS. **Note:** a note comes here | 
 **nsd_name** | **str**| Name of the ND Descriptor | 
 **vim_name** | **str**| Name of the VIM | 
 **k8s_namespace** | **str**| Name of the Namespace in Kubernetes (K8s) | 
 **kns_name** | **str**| Name of the KNS | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

