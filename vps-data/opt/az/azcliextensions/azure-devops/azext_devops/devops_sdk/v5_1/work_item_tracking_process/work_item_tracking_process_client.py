# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class WorkItemTrackingProcessClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingProcessClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '5264459e-e5e0-4bd8-b118-0985e68a4ec5'

    def create_process_behavior(self, behavior, process_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        content = self._serialize.body(behavior, 'ProcessBehaviorCreateRequest')
        response = self._send(http_method='POST',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessBehavior', response)

    def delete_process_behavior(self, process_id, behavior_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_process_behavior(self, process_id, behavior_ref_name, expand=None):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProcessBehavior', response)

    def get_process_behaviors(self, process_id, expand=None):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ProcessBehavior]', self._unwrap_collection(response))

    def update_process_behavior(self, behavior_data, process_id, behavior_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        content = self._serialize.body(behavior_data, 'ProcessBehaviorUpdateRequest')
        response = self._send(http_method='PUT',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessBehavior', response)

    def create_control_in_group(self, control, process_id, wit_ref_name, group_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        content = self._serialize.body(control, 'Control')
        response = self._send(http_method='POST',
                              location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Control', response)

    def move_control_to_group(self, control, process_id, wit_ref_name, group_id, control_id, remove_from_group_id=None):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if control_id is not None:
            route_values['controlId'] = self._serialize.url('control_id', control_id, 'str')
        query_parameters = {}
        if remove_from_group_id is not None:
            query_parameters['removeFromGroupId'] = self._serialize.query('remove_from_group_id', remove_from_group_id, 'str')
        content = self._serialize.body(control, 'Control')
        response = self._send(http_method='PUT',
                              location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Control', response)

    def remove_control_from_group(self, process_id, wit_ref_name, group_id, control_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if control_id is not None:
            route_values['controlId'] = self._serialize.url('control_id', control_id, 'str')
        self._send(http_method='DELETE',
                   location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_control(self, control, process_id, wit_ref_name, group_id, control_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        if control_id is not None:
            route_values['controlId'] = self._serialize.url('control_id', control_id, 'str')
        content = self._serialize.body(control, 'Control')
        response = self._send(http_method='PATCH',
                              location_id='1f59b363-a2d0-4b7e-9bc6-eb9f5f3f0e58',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Control', response)

    def add_field_to_work_item_type(self, field, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(field, 'AddProcessWorkItemTypeFieldRequest')
        response = self._send(http_method='POST',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemTypeField', response)

    def get_all_work_item_type_fields(self, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[ProcessWorkItemTypeField]', self._unwrap_collection(response))

    def get_work_item_type_field(self, process_id, wit_ref_name, field_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if field_ref_name is not None:
            route_values['fieldRefName'] = self._serialize.url('field_ref_name', field_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('ProcessWorkItemTypeField', response)

    def remove_work_item_type_field(self, process_id, wit_ref_name, field_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if field_ref_name is not None:
            route_values['fieldRefName'] = self._serialize.url('field_ref_name', field_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                   version='5.1-preview.2',
                   route_values=route_values)

    def update_work_item_type_field(self, field, process_id, wit_ref_name, field_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if field_ref_name is not None:
            route_values['fieldRefName'] = self._serialize.url('field_ref_name', field_ref_name, 'str')
        content = self._serialize.body(field, 'UpdateProcessWorkItemTypeFieldRequest')
        response = self._send(http_method='PATCH',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemTypeField', response)

    def add_group(self, group, process_id, wit_ref_name, page_id, section_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='POST',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Group', response)

    def move_group_to_page(self, group, process_id, wit_ref_name, page_id, section_id, group_id, remove_from_page_id, remove_from_section_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        query_parameters = {}
        if remove_from_page_id is not None:
            query_parameters['removeFromPageId'] = self._serialize.query('remove_from_page_id', remove_from_page_id, 'str')
        if remove_from_section_id is not None:
            query_parameters['removeFromSectionId'] = self._serialize.query('remove_from_section_id', remove_from_section_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='PUT',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Group', response)

    def move_group_to_section(self, group, process_id, wit_ref_name, page_id, section_id, group_id, remove_from_section_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        query_parameters = {}
        if remove_from_section_id is not None:
            query_parameters['removeFromSectionId'] = self._serialize.query('remove_from_section_id', remove_from_section_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='PUT',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Group', response)

    def remove_group(self, process_id, wit_ref_name, page_id, section_id, group_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        self._send(http_method='DELETE',
                   location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_group(self, group, process_id, wit_ref_name, page_id, section_id, group_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        if section_id is not None:
            route_values['sectionId'] = self._serialize.url('section_id', section_id, 'str')
        if group_id is not None:
            route_values['groupId'] = self._serialize.url('group_id', group_id, 'str')
        content = self._serialize.body(group, 'Group')
        response = self._send(http_method='PATCH',
                              location_id='766e44e1-36a8-41d7-9050-c343ff02f7a5',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Group', response)

    def get_form_layout(self, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='fa8646eb-43cd-4b71-9564-40106fd63e40',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FormLayout', response)

    def create_list(self, picklist):
        content = self._serialize.body(picklist, 'PickList')
        response = self._send(http_method='POST',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1',
                              content=content)
        return self._deserialize('PickList', response)

    def delete_list(self, list_id):
        route_values = {}
        if list_id is not None:
            route_values['listId'] = self._serialize.url('list_id', list_id, 'str')
        self._send(http_method='DELETE',
                   location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_list(self, list_id):
        route_values = {}
        if list_id is not None:
            route_values['listId'] = self._serialize.url('list_id', list_id, 'str')
        response = self._send(http_method='GET',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('PickList', response)

    def get_lists_metadata(self):
        response = self._send(http_method='GET',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1')
        return self._deserialize('[PickListMetadata]', self._unwrap_collection(response))

    def update_list(self, picklist, list_id):
        route_values = {}
        if list_id is not None:
            route_values['listId'] = self._serialize.url('list_id', list_id, 'str')
        content = self._serialize.body(picklist, 'PickList')
        response = self._send(http_method='PUT',
                              location_id='01e15468-e27c-4e20-a974-bd957dcccebc',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('PickList', response)

    def add_page(self, page, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(page, 'Page')
        response = self._send(http_method='POST',
                              location_id='1cc7b29f-6697-4d9d-b0a1-2650d3e1d584',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Page', response)

    def remove_page(self, process_id, wit_ref_name, page_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if page_id is not None:
            route_values['pageId'] = self._serialize.url('page_id', page_id, 'str')
        self._send(http_method='DELETE',
                   location_id='1cc7b29f-6697-4d9d-b0a1-2650d3e1d584',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_page(self, page, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(page, 'Page')
        response = self._send(http_method='PATCH',
                              location_id='1cc7b29f-6697-4d9d-b0a1-2650d3e1d584',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Page', response)

    def create_new_process(self, create_request):
        content = self._serialize.body(create_request, 'CreateProcessModel')
        response = self._send(http_method='POST',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              content=content)
        return self._deserialize('ProcessInfo', response)

    def delete_process_by_id(self, process_type_id):
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        self._send(http_method='DELETE',
                   location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                   version='5.1-preview.2',
                   route_values=route_values)

    def edit_process(self, update_request, process_type_id):
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        content = self._serialize.body(update_request, 'UpdateProcessModel')
        response = self._send(http_method='PATCH',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessInfo', response)

    def get_list_of_processes(self, expand=None):
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              query_parameters=query_parameters)
        return self._deserialize('[ProcessInfo]', self._unwrap_collection(response))

    def get_process_by_its_id(self, process_type_id, expand=None):
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProcessInfo', response)

    def add_process_work_item_type_rule(self, process_rule_create, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(process_rule_create, 'CreateProcessRuleRequest')
        response = self._send(http_method='POST',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessRule', response)

    def delete_process_work_item_type_rule(self, process_id, wit_ref_name, rule_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        self._send(http_method='DELETE',
                   location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_process_work_item_type_rule(self, process_id, wit_ref_name, rule_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        response = self._send(http_method='GET',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('ProcessRule', response)

    def get_process_work_item_type_rules(self, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values)
        return self._deserialize('[ProcessRule]', self._unwrap_collection(response))

    def update_process_work_item_type_rule(self, process_rule, process_id, wit_ref_name, rule_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        content = self._serialize.body(process_rule, 'UpdateProcessRuleRequest')
        response = self._send(http_method='PUT',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessRule', response)

    def create_state_definition(self, state_model, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(state_model, 'WorkItemStateInputModel')
        response = self._send(http_method='POST',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemStateResultModel', response)

    def delete_state_definition(self, process_id, wit_ref_name, state_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        self._send(http_method='DELETE',
                   location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_state_definition(self, process_id, wit_ref_name, state_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        response = self._send(http_method='GET',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemStateResultModel', response)

    def get_state_definitions(self, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemStateResultModel]', self._unwrap_collection(response))

    def hide_state_definition(self, hide_state_model, process_id, wit_ref_name, state_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        content = self._serialize.body(hide_state_model, 'HideStateModel')
        response = self._send(http_method='PUT',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemStateResultModel', response)

    def update_state_definition(self, state_model, process_id, wit_ref_name, state_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        content = self._serialize.body(state_model, 'WorkItemStateInputModel')
        response = self._send(http_method='PATCH',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemStateResultModel', response)

    def create_process_work_item_type(self, work_item_type, process_id):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        content = self._serialize.body(work_item_type, 'CreateProcessWorkItemTypeRequest')
        response = self._send(http_method='POST',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemType', response)

    def delete_process_work_item_type(self, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                   version='5.1-preview.2',
                   route_values=route_values)

    def get_process_work_item_type(self, process_id, wit_ref_name, expand=None):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProcessWorkItemType', response)

    def get_process_work_item_types(self, process_id, expand=None):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ProcessWorkItemType]', self._unwrap_collection(response))

    def update_process_work_item_type(self, work_item_type_update, process_id, wit_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(work_item_type_update, 'UpdateProcessWorkItemTypeRequest')
        response = self._send(http_method='PATCH',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='5.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessWorkItemType', response)

    def add_behavior_to_work_item_type(self, behavior, process_id, wit_ref_name_for_behaviors):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        content = self._serialize.body(behavior, 'WorkItemTypeBehavior')
        response = self._send(http_method='POST',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTypeBehavior', response)

    def get_behavior_for_work_item_type(self, process_id, wit_ref_name_for_behaviors, behavior_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemTypeBehavior', response)

    def get_behaviors_for_work_item_type(self, process_id, wit_ref_name_for_behaviors):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        response = self._send(http_method='GET',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemTypeBehavior]', self._unwrap_collection(response))

    def remove_behavior_from_work_item_type(self, process_id, wit_ref_name_for_behaviors, behavior_ref_name):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                   version='5.1-preview.1',
                   route_values=route_values)

    def update_behavior_to_work_item_type(self, behavior, process_id, wit_ref_name_for_behaviors):
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name_for_behaviors is not None:
            route_values['witRefNameForBehaviors'] = self._serialize.url('wit_ref_name_for_behaviors', wit_ref_name_for_behaviors, 'str')
        content = self._serialize.body(behavior, 'WorkItemTypeBehavior')
        response = self._send(http_method='PATCH',
                              location_id='6d765a2e-4e1b-4b11-be93-f953be676024',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTypeBehavior', response)

