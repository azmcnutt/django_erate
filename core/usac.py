import requests
from datetime import datetime
from zoneinfo import ZoneInfo
from pprint import pprint

from odata.service import ODataService, Query


class Usac:
    def __init__(self, url = 'https://opendata.usac.org/api/odata/v4/'):
        self.odata_url = url
        self.session = requests.Session()
        self.odata_service = ODataService(self.odata_url, reflect_entities=True, session=self.session)
        self.entity = self._Entity(self.odata_service)
        self.annex = self._Annex(self.odata_service)
    

    class _Entity:
        def __init__(self, odata_service, **kwargs):
            self.odata_service = odata_service
            self.entity_info = self.odata_service.entities['7i5i-83qf']
            if ben := kwargs.get('ben', None):
                self.set_ben(ben)
        
        def set_ben(self, ben):
            self.entity = self.get_ben(ben)
            if not self.entity:
                return None
        
        def get_ben(self, ben):
            date_attr = [
                'fcc_form_498_status_date_time',
                'last_updated_date',
            ]
            billed_entity_search = self.odata_service.query(self.entity_info)
            billed_entity_search = billed_entity_search.filter(self.entity_info.entity_number == str(ben))
            entity = {}
            for billed_entity in billed_entity_search:
                entity['id'] = getattr(billed_entity, '__id')
                for attr in dir(billed_entity):
                    if (
                        not attr.startswith('__') 
                        and not attr.startswith('parent_entity')
                        and attr not in entity
                    ):
                        if attr in date_attr:
                            if getattr(billed_entity, attr):
                                try:
                                    entity[attr] = datetime.fromisoformat(getattr(billed_entity, attr)).replace(tzinfo=ZoneInfo("America/New_York"))
                                except ValueError:
                                    print('e')
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
    

    class _Annex:
        def __init__(self, odata_service, **kwargs):
            self.odata_service = odata_service
            self.annex_info = self.odata_service.entities['hwzi-t5nj']
        
        def get_annexes(self, ben):
            date_attr = [
                'last_updated_date',
            ]
            annex_search = self.odata_service.query(self.annex_info)
            annex_search = annex_search.filter(self.annex_info.annex_parent_organization_number == str(ben))
            annexes = []
            for annex in annex_search:
                temp_annex = {}
                temp_annex['id'] = getattr(annex, '__id')
                for attr in dir(annex):
                    if (
                        not attr.startswith('__') 
                        and not attr.startswith('parent_entity')
                        and attr not in temp_annex
                    ):
                        if attr in date_attr:
                            if getattr(annex, attr):
                                try:
                                    temp_annex[attr] = datetime.fromisoformat(getattr(annex, attr)).replace(tzinfo=ZoneInfo("America/New_York"))
                                except ValueError:
                                    temp_annex[attr] = getattr(annex, attr)
                        else:
                            temp_annex[attr] = getattr(annex, attr)
                annexes.append(temp_annex)                
            if annexes:
                return annexes
            else:
                return None
