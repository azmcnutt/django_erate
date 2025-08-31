import requests
from datetime import datetime
from odata.service import ODataService, Query

class OData:
    def __init__(self, url = 'https://opendata.usac.org/api/odata/v4/'):
        self.odata_url = url
        self.session = requests.Session()
        self.odata_service = ODataService(self.odata_url, reflect_entities=True, session=self.session)
        self.entity_info = self.odata_service.entities['7i5i-83qf']

    def get_ben(self, ben):
        date_attr = [
            'fcc_form_498_status_date_time',
            'last_updated_date',
        ]
        billed_entity_search = self.odata_service.query(self.entity_info)
        # query = query.filter(customers.physical_county.__eq__('Mohave'))
        # billed_entity_search = billed_entity_search.filter(entity.entity_number.startswith('143220'))
        billed_entity_search = billed_entity_search.filter(self.entity_info.entity_number == str(ben))
        # billed_entity_search = billed_entity_search.filter(entity.entity_number.__eq__('212700'))
        # if not billed_entity_search:
        #     print('not found')
        # str.startswith
        entity = {}
        for billed_entity in billed_entity_search:
            billed_entity
            for attr in dir(billed_entity):
                if (
                    not attr.startswith('__') 
                    and not attr.startswith('parent_entity')
                    and attr not in entity
                ):
                    if attr in date_attr:
                        if getattr(billed_entity, attr):
                            try:
                                entity[attr] = datetime.fromisoformat(getattr(billed_entity, attr).replace('Z', '+00:00'))
                            except ValueError:
                                entity[attr] = getattr(billed_entity, attr)
                    else:
                        entity[attr] = getattr(billed_entity, attr)
            # if 'ben' not in entity:
            #     entity['ben'] = billed_entity.entity_number
            # if 'name' not in entity:
            #     entity['name'] = billed_entity.entity_name
            if billed_entity.parent_entity_number:
                if 'parent_entities' not in entity:
                    entity['parent_entities'] = [(billed_entity.parent_entity_number, billed_entity.parent_entity_name), ]
                else:
                    entity['parent_entities'].append((billed_entity.parent_entity_number, billed_entity.parent_entity_name))
        if entity:
            child_entity_search = self.odata_service.query(self.entity_info)
            child_entity_search = child_entity_search.filter(self.entity_info.parent_entity_number.__eq__(entity['entity_number']))
            for child_entity in child_entity_search:
                if 'child_entities' not in entity:
                    entity['child_entities'] = [(child_entity.entity_number, child_entity.entity_name), ]
                else:
                    entity['child_entities'].append((child_entity.entity_number, child_entity.entity_name))
            
        if entity:
            return entity
        else:
            return None

class Billed_Entity:
    def __init__(self, ben):
        usac = OData()
        self.entity = usac.get_ben(ben)
        if not self.entity:
            raise BenNotFoundError(f'BEN {ben} not found')
    
    @property
    def all(self):
        return self.entity
    
    @property
    def entity_name(self):
        return self.entity['entity_name']

    @property
    def entity_number(self):
        return self.entity['entity_number']

    @property
    def entity_type(self):
        return self.entity['entity_type']

    @property
    def parent_entities(self):
        if 'parent_entities' in self.entity.keys():
            return self.entity['parent_entities']
        else:
            return None

    @property
    def child_entities(self):
        if 'child_entities' in self.entity.keys():
            return self.entity['child_entities']
        else:
            return None

class BenNotFoundError(Exception):
    """Custom exception raised when a billed entity number is not found."""
    def __init__(self, message="BEN not found"):
        self.message = message
        super().__init__(self.message)