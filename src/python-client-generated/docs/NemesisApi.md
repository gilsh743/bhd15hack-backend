# swagger_client.NemesisApi

All URIs are relative to *https://babeltower/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_raw_attachment_by_id**](NemesisApi.md#get_raw_attachment_by_id) | **GET** /nms/document/attachment/raw/{attachment_id} | 
[**get_raw_document_by_id**](NemesisApi.md#get_raw_document_by_id) | **GET** /nms/document/raw/{document_id} | 

# **get_raw_attachment_by_id**
> TextFile get_raw_attachment_by_id(attachment_id)



Get **raw** attachment by its id. Note that a single nemsis document may have multiple attachments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: nms_auth
configuration = swagger_client.Configuration()
configuration.api_key['nms_cookie'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['nms_cookie'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NemesisApi(swagger_client.ApiClient(configuration))
attachment_id = 'attachment_id_example' # str | The id of the document's attachment itself.

try:
    api_response = api_instance.get_raw_attachment_by_id(attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NemesisApi->get_raw_attachment_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment_id** | **str**| The id of the document&#x27;s attachment itself. | 

### Return type

[**TextFile**](TextFile.md)

### Authorization

[nms_auth](../README.md#nms_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_raw_document_by_id**
> TextFile get_raw_document_by_id(document_id)



Get **raw** text by a document id. Note that this requests will combine all attachments together.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: nms_auth
configuration = swagger_client.Configuration()
configuration.api_key['nms_cookie'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['nms_cookie'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.NemesisApi(swagger_client.ApiClient(configuration))
document_id = 'document_id_example' # str | The id of the document as presented in Nemesis.

try:
    api_response = api_instance.get_raw_document_by_id(document_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NemesisApi->get_raw_document_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_id** | **str**| The id of the document as presented in Nemesis. | 

### Return type

[**TextFile**](TextFile.md)

### Authorization

[nms_auth](../README.md#nms_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

