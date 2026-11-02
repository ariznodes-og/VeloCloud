# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class GalleryClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(GalleryClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '69d21c00-f135-441b-b5ce-3626378e0819'

    def share_extension_by_id(self, extension_id, account_name):
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='POST',
                   location_id='1f19631b-a0b4-4a03-89c2-d79785d24360',
                   version='6.0-preview.1',
                   route_values=route_values)

    def unshare_extension_by_id(self, extension_id, account_name):
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='DELETE',
                   location_id='1f19631b-a0b4-4a03-89c2-d79785d24360',
                   version='6.0-preview.1',
                   route_values=route_values)

    def share_extension(self, publisher_name, extension_name, account_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='POST',
                   location_id='a1e66d8f-f5de-4d16-8309-91a4e015ee46',
                   version='6.0-preview.1',
                   route_values=route_values)

    def unshare_extension(self, publisher_name, extension_name, account_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if account_name is not None:
            route_values['accountName'] = self._serialize.url('account_name', account_name, 'str')
        self._send(http_method='DELETE',
                   location_id='a1e66d8f-f5de-4d16-8309-91a4e015ee46',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_acquisition_options(self, item_id, installation_target, test_commerce=None, is_free_or_trial_install=None):
        route_values = {}
        if item_id is not None:
            route_values['itemId'] = self._serialize.url('item_id', item_id, 'str')
        query_parameters = {}
        if installation_target is not None:
            query_parameters['installationTarget'] = self._serialize.query('installation_target', installation_target, 'str')
        if test_commerce is not None:
            query_parameters['testCommerce'] = self._serialize.query('test_commerce', test_commerce, 'bool')
        if is_free_or_trial_install is not None:
            query_parameters['isFreeOrTrialInstall'] = self._serialize.query('is_free_or_trial_install', is_free_or_trial_install, 'bool')
        response = self._send(http_method='GET',
                              location_id='9d0a0105-075e-4760-aa15-8bcf54d1bd7d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('AcquisitionOptions', response)

    def request_acquisition(self, acquisition_request):
        content = self._serialize.body(acquisition_request, 'ExtensionAcquisitionRequest')
        response = self._send(http_method='POST',
                              location_id='3adb1f2d-e328-446e-be73-9f6d98071c45',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('ExtensionAcquisitionRequest', response)

    def get_asset_by_name(self, publisher_name, extension_name, version, asset_type, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='7529171f-a002-4180-93ba-685f358a0482',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset(self, extension_id, version, asset_type, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='5d545f3d-ef47-488b-8be3-f5ee1517856c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset_authenticated(self, publisher_name, extension_name, version, asset_type, account_token=None, account_token_header=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='506aff36-2622-4f70-8063-77cce6366d20',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def associate_azure_publisher(self, publisher_name, azure_publisher_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if azure_publisher_id is not None:
            query_parameters['azurePublisherId'] = self._serialize.query('azure_publisher_id', azure_publisher_id, 'str')
        response = self._send(http_method='PUT',
                              location_id='efd202a6-9d87-4ebc-9229-d2b8ae2fdb6d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('AzurePublisher', response)

    def query_associated_azure_publisher(self, publisher_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        response = self._send(http_method='GET',
                              location_id='efd202a6-9d87-4ebc-9229-d2b8ae2fdb6d',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('AzurePublisher', response)

    def get_categories(self, languages=None):
        query_parameters = {}
        if languages is not None:
            query_parameters['languages'] = self._serialize.query('languages', languages, 'str')
        response = self._send(http_method='GET',
                              location_id='e0a5a71e-3ac3-43a0-ae7d-0bb5c3046a2a',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[str]', self._unwrap_collection(response))

    def get_category_details(self, category_name, languages=None, product=None):
        route_values = {}
        if category_name is not None:
            route_values['categoryName'] = self._serialize.url('category_name', category_name, 'str')
        query_parameters = {}
        if languages is not None:
            query_parameters['languages'] = self._serialize.query('languages', languages, 'str')
        if product is not None:
            query_parameters['product'] = self._serialize.query('product', product, 'str')
        response = self._send(http_method='GET',
                              location_id='75d3c04d-84d2-4973-acd2-22627587dabc',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CategoriesResult', response)

    def get_category_tree(self, product, category_id, lcid=None, source=None, product_version=None, skus=None, sub_skus=None):
        route_values = {}
        if product is not None:
            route_values['product'] = self._serialize.url('product', product, 'str')
        if category_id is not None:
            route_values['categoryId'] = self._serialize.url('category_id', category_id, 'str')
        query_parameters = {}
        if lcid is not None:
            query_parameters['lcid'] = self._serialize.query('lcid', lcid, 'int')
        if source is not None:
            query_parameters['source'] = self._serialize.query('source', source, 'str')
        if product_version is not None:
            query_parameters['productVersion'] = self._serialize.query('product_version', product_version, 'str')
        if skus is not None:
            query_parameters['skus'] = self._serialize.query('skus', skus, 'str')
        if sub_skus is not None:
            query_parameters['subSkus'] = self._serialize.query('sub_skus', sub_skus, 'str')
        response = self._send(http_method='GET',
                              location_id='1102bb42-82b0-4955-8d8a-435d6b4cedd3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProductCategory', response)

    def get_root_categories(self, product, lcid=None, source=None, product_version=None, skus=None, sub_skus=None):
        route_values = {}
        if product is not None:
            route_values['product'] = self._serialize.url('product', product, 'str')
        query_parameters = {}
        if lcid is not None:
            query_parameters['lcid'] = self._serialize.query('lcid', lcid, 'int')
        if source is not None:
            query_parameters['source'] = self._serialize.query('source', source, 'str')
        if product_version is not None:
            query_parameters['productVersion'] = self._serialize.query('product_version', product_version, 'str')
        if skus is not None:
            query_parameters['skus'] = self._serialize.query('skus', skus, 'str')
        if sub_skus is not None:
            query_parameters['subSkus'] = self._serialize.query('sub_skus', sub_skus, 'str')
        response = self._send(http_method='GET',
                              location_id='31fba831-35b2-46f6-a641-d05de5a877d8',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProductCategoriesResult', response)

    def get_certificate(self, publisher_name, extension_name, version=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='e905ad6a-3f1f-4d08-9f6d-7d357ff8b7d0',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_content_verification_log(self, publisher_name, extension_name, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        response = self._send(http_method='GET',
                              location_id='c0f1c7c4-3557-4ffb-b774-1e48c4865e99',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_draft_for_edit_extension(self, publisher_name, extension_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        response = self._send(http_method='POST',
                              location_id='02b33873-4e61-496e-83a2-59d1df46b7d8',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ExtensionDraft', response)

    def perform_edit_extension_draft_operation(self, draft_patch, publisher_name, extension_name, draft_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        content = self._serialize.body(draft_patch, 'ExtensionDraftPatch')
        response = self._send(http_method='PATCH',
                              location_id='02b33873-4e61-496e-83a2-59d1df46b7d8',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ExtensionDraft', response)

    def update_payload_in_draft_for_edit_extension(self, upload_stream, publisher_name, extension_name, draft_id, file_name=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        additional_headers = {}
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='02b33873-4e61-496e-83a2-59d1df46b7d8',
                              version='6.0-preview.1',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraft', response)

    def add_asset_for_edit_extension_draft(self, upload_stream, publisher_name, extension_name, draft_id, asset_type, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='f1db9c47-6619-4998-a7e5-d7f9f41a4617',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraftAsset', response)

    def create_draft_for_new_extension(self, upload_stream, publisher_name, product, file_name=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        additional_headers = {}
        if product is not None:
            additional_headers['X-Market-UploadFileProduct'] = product
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='b3ab127d-ebb9-4d22-b611-4e09593c8d79',
                              version='6.0-preview.1',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraft', response)

    def perform_new_extension_draft_operation(self, draft_patch, publisher_name, draft_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        content = self._serialize.body(draft_patch, 'ExtensionDraftPatch')
        response = self._send(http_method='PATCH',
                              location_id='b3ab127d-ebb9-4d22-b611-4e09593c8d79',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ExtensionDraft', response)

    def update_payload_in_draft_for_new_extension(self, upload_stream, publisher_name, draft_id, file_name=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        additional_headers = {}
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='b3ab127d-ebb9-4d22-b611-4e09593c8d79',
                              version='6.0-preview.1',
                              route_values=route_values,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraft', response)

    def add_asset_for_new_extension_draft(self, upload_stream, publisher_name, draft_id, asset_type, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='88c0b1c8-b4f1-498a-9b2a-8446ef9f32e7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('ExtensionDraftAsset', response)

    def get_asset_from_edit_extension_draft(self, publisher_name, draft_id, asset_type, extension_name, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        query_parameters = {}
        if extension_name is not None:
            query_parameters['extensionName'] = self._serialize.query('extension_name', extension_name, 'str')
        response = self._send(http_method='GET',
                              location_id='88c0b1c8-b4f1-498a-9b2a-8446ef9f32e7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset_from_new_extension_draft(self, publisher_name, draft_id, asset_type, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if draft_id is not None:
            route_values['draftId'] = self._serialize.url('draft_id', draft_id, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        response = self._send(http_method='GET',
                              location_id='88c0b1c8-b4f1-498a-9b2a-8446ef9f32e7',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_extension_events(self, publisher_name, extension_name, count=None, after_date=None, include=None, include_property=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        if include is not None:
            query_parameters['include'] = self._serialize.query('include', include, 'str')
        if include_property is not None:
            query_parameters['includeProperty'] = self._serialize.query('include_property', include_property, 'str')
        response = self._send(http_method='GET',
                              location_id='3d13c499-2168-4d06-bef4-14aba185dcd5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ExtensionEvents', response)

    def publish_extension_events(self, extension_events):
        content = self._serialize.body(extension_events, '[ExtensionEvents]')
        self._send(http_method='POST',
                   location_id='0bf2bd3a-70e0-4d5d-8bf7-bd4a9c2ab6e7',
                   version='6.0-preview.1',
                   content=content)

    def query_extensions(self, extension_query, account_token=None, account_token_header=None):
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        content = self._serialize.body(extension_query, 'ExtensionQuery')
        response = self._send(http_method='POST',
                              location_id='eb9d5ee1-6d43-456b-b80e-8a96fbc014b6',
                              version='6.0-preview.1',
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              content=content)
        return self._deserialize('ExtensionQueryResult', response)

    def create_extension(self, upload_stream, **kwargs):
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                              version='6.0-preview.2',
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('PublishedExtension', response)

    def delete_extension_by_id(self, extension_id, version=None):
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                   version='6.0-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_extension_by_id(self, extension_id, version=None, flags=None):
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'str')
        response = self._send(http_method='GET',
                              location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PublishedExtension', response)

    def update_extension_by_id(self, extension_id):
        route_values = {}
        if extension_id is not None:
            route_values['extensionId'] = self._serialize.url('extension_id', extension_id, 'str')
        response = self._send(http_method='PUT',
                              location_id='a41192c8-9525-4b58-bc86-179fa549d80d',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('PublishedExtension', response)

    def create_extension_with_publisher(self, upload_stream, publisher_name, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('PublishedExtension', response)

    def delete_extension(self, publisher_name, extension_name, version=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        self._send(http_method='DELETE',
                   location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                   version='6.0-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_extension(self, publisher_name, extension_name, version=None, flags=None, account_token=None, account_token_header=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if version is not None:
            query_parameters['version'] = self._serialize.query('version', version, 'str')
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'str')
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers)
        return self._deserialize('PublishedExtension', response)

    def update_extension(self, upload_stream, publisher_name, extension_name, bypass_scope_check=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if bypass_scope_check is not None:
            query_parameters['bypassScopeCheck'] = self._serialize.query('bypass_scope_check', bypass_scope_check, 'bool')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('PublishedExtension', response)

    def update_extension_properties(self, publisher_name, extension_name, flags):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'str')
        response = self._send(http_method='PATCH',
                              location_id='e11ea35a-16fe-4b80-ab11-c4cab88a0966',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PublishedExtension', response)

    def share_extension_with_host(self, publisher_name, extension_name, host_type, host_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if host_type is not None:
            route_values['hostType'] = self._serialize.url('host_type', host_type, 'str')
        if host_name is not None:
            route_values['hostName'] = self._serialize.url('host_name', host_name, 'str')
        self._send(http_method='POST',
                   location_id='328a3af8-d124-46e9-9483-01690cd415b9',
                   version='6.0-preview.1',
                   route_values=route_values)

    def unshare_extension_with_host(self, publisher_name, extension_name, host_type, host_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if host_type is not None:
            route_values['hostType'] = self._serialize.url('host_type', host_type, 'str')
        if host_name is not None:
            route_values['hostName'] = self._serialize.url('host_name', host_name, 'str')
        self._send(http_method='DELETE',
                   location_id='328a3af8-d124-46e9-9483-01690cd415b9',
                   version='6.0-preview.1',
                   route_values=route_values)

    def extension_validator(self, azure_rest_api_request_model):
        content = self._serialize.body(azure_rest_api_request_model, 'AzureRestApiRequestModel')
        self._send(http_method='POST',
                   location_id='05e8a5e1-8c59-4c2c-8856-0ff087d1a844',
                   version='6.0-preview.1',
                   content=content)

    def send_notifications(self, notification_data):
        content = self._serialize.body(notification_data, 'NotificationsData')
        self._send(http_method='POST',
                   location_id='eab39817-413c-4602-a49f-07ad00844980',
                   version='6.0-preview.1',
                   content=content)

    def get_package(self, publisher_name, extension_name, version, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='7cb576f8-1cae-4c4b-b7b1-e4af5759e965',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_asset_with_token(self, publisher_name, extension_name, version, asset_type, asset_token=None, account_token=None, accept_default=None, account_token_header=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        if asset_type is not None:
            route_values['assetType'] = self._serialize.url('asset_type', asset_type, 'str')
        if asset_token is not None:
            route_values['assetToken'] = self._serialize.url('asset_token', asset_token, 'str')
        query_parameters = {}
        if account_token is not None:
            query_parameters['accountToken'] = self._serialize.query('account_token', account_token, 'str')
        if accept_default is not None:
            query_parameters['acceptDefault'] = self._serialize.query('accept_default', accept_default, 'bool')
        additional_headers = {}
        if account_token_header is not None:
            additional_headers['X-Market-AccountToken'] = account_token_header
        response = self._send(http_method='GET',
                              location_id='364415a1-0077-4a41-a7a0-06edd4497492',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def delete_publisher_asset(self, publisher_name, asset_type=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if asset_type is not None:
            query_parameters['assetType'] = self._serialize.query('asset_type', asset_type, 'str')
        self._send(http_method='DELETE',
                   location_id='21143299-34f9-4c62-8ca8-53da691192f9',
                   version='6.0-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_publisher_asset(self, publisher_name, asset_type=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if asset_type is not None:
            query_parameters['assetType'] = self._serialize.query('asset_type', asset_type, 'str')
        response = self._send(http_method='GET',
                              location_id='21143299-34f9-4c62-8ca8-53da691192f9',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def update_publisher_asset(self, upload_stream, publisher_name, asset_type=None, file_name=None, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if asset_type is not None:
            query_parameters['assetType'] = self._serialize.query('asset_type', asset_type, 'str')
        additional_headers = {}
        if file_name is not None:
            additional_headers['X-Market-UploadFileName'] = file_name
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='21143299-34f9-4c62-8ca8-53da691192f9',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('{str}', self._unwrap_collection(response))

    def query_publishers(self, publisher_query):
        content = self._serialize.body(publisher_query, 'PublisherQuery')
        response = self._send(http_method='POST',
                              location_id='2ad6ee0a-b53f-4034-9d1d-d009fda1212e',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('PublisherQueryResult', response)

    def create_publisher(self, publisher):
        content = self._serialize.body(publisher, 'Publisher')
        response = self._send(http_method='POST',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('Publisher', response)

    def delete_publisher(self, publisher_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        self._send(http_method='DELETE',
                   location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_publisher(self, publisher_name, flags=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if flags is not None:
            query_parameters['flags'] = self._serialize.query('flags', flags, 'int')
        response = self._send(http_method='GET',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Publisher', response)

    def update_publisher(self, publisher, publisher_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        content = self._serialize.body(publisher, 'Publisher')
        response = self._send(http_method='PUT',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Publisher', response)

    def update_publisher_members(self, role_assignments, publisher_name, limit_to_caller_identity_domain=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        query_parameters = {}
        if limit_to_caller_identity_domain is not None:
            query_parameters['limitToCallerIdentityDomain'] = self._serialize.query('limit_to_caller_identity_domain', limit_to_caller_identity_domain, 'bool')
        content = self._serialize.body(role_assignments, '[PublisherUserRoleAssignmentRef]')
        response = self._send(http_method='POST',
                              location_id='4ddec66a-e4f6-4f5d-999e-9e77710d7ff4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('[PublisherRoleAssignment]', self._unwrap_collection(response))

    def get_questions(self, publisher_name, extension_name, count=None, page=None, after_date=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if page is not None:
            query_parameters['page'] = self._serialize.query('page', page, 'int')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='c010d03d-812c-4ade-ae07-c1862475eda5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('QuestionsResult', response)

    def report_question(self, concern, pub_name, ext_name, question_id):
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        content = self._serialize.body(concern, 'Concern')
        response = self._send(http_method='POST',
                              location_id='784910cd-254a-494d-898b-0728549b2f10',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Concern', response)

    def create_question(self, question, publisher_name, extension_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        content = self._serialize.body(question, 'Question')
        response = self._send(http_method='POST',
                              location_id='6d1d9741-eca8-4701-a3a5-235afc82dfa4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Question', response)

    def delete_question(self, publisher_name, extension_name, question_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        self._send(http_method='DELETE',
                   location_id='6d1d9741-eca8-4701-a3a5-235afc82dfa4',
                   version='6.0-preview.1',
                   route_values=route_values)

    def update_question(self, question, publisher_name, extension_name, question_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        content = self._serialize.body(question, 'Question')
        response = self._send(http_method='PATCH',
                              location_id='6d1d9741-eca8-4701-a3a5-235afc82dfa4',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Question', response)

    def create_response(self, response, publisher_name, extension_name, question_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        content = self._serialize.body(response, 'Response')
        response = self._send(http_method='POST',
                              location_id='7f8ae5e0-46b0-438f-b2e8-13e8513517bd',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Response', response)

    def delete_response(self, publisher_name, extension_name, question_id, response_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        if response_id is not None:
            route_values['responseId'] = self._serialize.url('response_id', response_id, 'long')
        self._send(http_method='DELETE',
                   location_id='7f8ae5e0-46b0-438f-b2e8-13e8513517bd',
                   version='6.0-preview.1',
                   route_values=route_values)

    def update_response(self, response, publisher_name, extension_name, question_id, response_id):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if question_id is not None:
            route_values['questionId'] = self._serialize.url('question_id', question_id, 'long')
        if response_id is not None:
            route_values['responseId'] = self._serialize.url('response_id', response_id, 'long')
        content = self._serialize.body(response, 'Response')
        response = self._send(http_method='PATCH',
                              location_id='7f8ae5e0-46b0-438f-b2e8-13e8513517bd',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Response', response)

    def get_extension_reports(self, publisher_name, extension_name, days=None, count=None, after_date=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if days is not None:
            query_parameters['days'] = self._serialize.query('days', days, 'int')
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='79e0c74f-157f-437e-845f-74fbb4121d4c',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('object', response)

    def get_reviews(self, publisher_name, extension_name, count=None, filter_options=None, before_date=None, after_date=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if count is not None:
            query_parameters['count'] = self._serialize.query('count', count, 'int')
        if filter_options is not None:
            query_parameters['filterOptions'] = self._serialize.query('filter_options', filter_options, 'str')
        if before_date is not None:
            query_parameters['beforeDate'] = self._serialize.query('before_date', before_date, 'iso-8601')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='5b3f819f-f247-42ad-8c00-dd9ab9ab246d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReviewsResult', response)

    def get_reviews_summary(self, pub_name, ext_name, before_date=None, after_date=None):
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        query_parameters = {}
        if before_date is not None:
            query_parameters['beforeDate'] = self._serialize.query('before_date', before_date, 'iso-8601')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='b7b44e21-209e-48f0-ae78-04727fc37d77',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReviewSummary', response)

    def create_review(self, review, pub_name, ext_name):
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        content = self._serialize.body(review, 'Review')
        response = self._send(http_method='POST',
                              location_id='e6e85b9d-aa70-40e6-aa28-d0fbf40b91a3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Review', response)

    def delete_review(self, pub_name, ext_name, review_id):
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        if review_id is not None:
            route_values['reviewId'] = self._serialize.url('review_id', review_id, 'long')
        self._send(http_method='DELETE',
                   location_id='e6e85b9d-aa70-40e6-aa28-d0fbf40b91a3',
                   version='6.0-preview.1',
                   route_values=route_values)

    def update_review(self, review_patch, pub_name, ext_name, review_id):
        route_values = {}
        if pub_name is not None:
            route_values['pubName'] = self._serialize.url('pub_name', pub_name, 'str')
        if ext_name is not None:
            route_values['extName'] = self._serialize.url('ext_name', ext_name, 'str')
        if review_id is not None:
            route_values['reviewId'] = self._serialize.url('review_id', review_id, 'long')
        content = self._serialize.body(review_patch, 'ReviewPatch')
        response = self._send(http_method='PATCH',
                              location_id='e6e85b9d-aa70-40e6-aa28-d0fbf40b91a3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReviewPatch', response)

    def create_category(self, category):
        content = self._serialize.body(category, 'ExtensionCategory')
        response = self._send(http_method='POST',
                              location_id='476531a3-7024-4516-a76a-ed64d3008ad6',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('ExtensionCategory', response)

    def get_gallery_user_settings(self, user_scope, key=None):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        if key is not None:
            route_values['key'] = self._serialize.url('key', key, 'str')
        response = self._send(http_method='GET',
                              location_id='9b75ece3-7960-401c-848b-148ac01ca350',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('{object}', self._unwrap_collection(response))

    def set_gallery_user_settings(self, entries, user_scope):
        route_values = {}
        if user_scope is not None:
            route_values['userScope'] = self._serialize.url('user_scope', user_scope, 'str')
        content = self._serialize.body(entries, '{object}')
        self._send(http_method='PATCH',
                   location_id='9b75ece3-7960-401c-848b-148ac01ca350',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content)

    def generate_key(self, key_type, expire_current_seconds=None):
        route_values = {}
        if key_type is not None:
            route_values['keyType'] = self._serialize.url('key_type', key_type, 'str')
        query_parameters = {}
        if expire_current_seconds is not None:
            query_parameters['expireCurrentSeconds'] = self._serialize.query('expire_current_seconds', expire_current_seconds, 'int')
        self._send(http_method='POST',
                   location_id='92ed5cf4-c38b-465a-9059-2f2fb7c624b5',
                   version='6.0-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_signing_key(self, key_type):
        route_values = {}
        if key_type is not None:
            route_values['keyType'] = self._serialize.url('key_type', key_type, 'str')
        response = self._send(http_method='GET',
                              location_id='92ed5cf4-c38b-465a-9059-2f2fb7c624b5',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def update_extension_statistics(self, extension_statistics_update, publisher_name, extension_name):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        content = self._serialize.body(extension_statistics_update, 'ExtensionStatisticUpdate')
        self._send(http_method='PATCH',
                   location_id='a0ea3204-11e9-422d-a9ca-45851cc41400',
                   version='6.0-preview.1',
                   route_values=route_values,
                   content=content)

    def get_extension_daily_stats(self, publisher_name, extension_name, days=None, aggregate=None, after_date=None):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        query_parameters = {}
        if days is not None:
            query_parameters['days'] = self._serialize.query('days', days, 'int')
        if aggregate is not None:
            query_parameters['aggregate'] = self._serialize.query('aggregate', aggregate, 'str')
        if after_date is not None:
            query_parameters['afterDate'] = self._serialize.query('after_date', after_date, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='ae06047e-51c5-4fb4-ab65-7be488544416',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ExtensionDailyStats', response)

    def get_extension_daily_stats_anonymous(self, publisher_name, extension_name, version):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='4fa7adb6-ca65-4075-a232-5f28323288ea',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('ExtensionDailyStats', response)

    def increment_extension_daily_stat(self, publisher_name, extension_name, version, stat_type):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        query_parameters = {}
        if stat_type is not None:
            query_parameters['statType'] = self._serialize.query('stat_type', stat_type, 'str')
        self._send(http_method='POST',
                   location_id='4fa7adb6-ca65-4075-a232-5f28323288ea',
                   version='6.0-preview.1',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_verification_log(self, publisher_name, extension_name, version, **kwargs):
        route_values = {}
        if publisher_name is not None:
            route_values['publisherName'] = self._serialize.url('publisher_name', publisher_name, 'str')
        if extension_name is not None:
            route_values['extensionName'] = self._serialize.url('extension_name', extension_name, 'str')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'str')
        response = self._send(http_method='GET',
                              location_id='c5523abe-b843-437f-875b-5833064efe4d',
                              version='6.0-preview.1',
                              route_values=route_values,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

