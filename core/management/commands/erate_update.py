from django.core.management.base import BaseCommand
from core.models import EntityInformation
from core.usac import Billed_Entity
import logging

logger = logging.getLogger(__name__)

UPDATED_BENS = []

def add_or_update_entity(ben):
    e = Billed_Entity(ben)
    e_obj = {}
    e_num = e.entity_number
    e_obj['entity_name'] = e.entity_name
    e_obj['entity_type'] = e.entity_type
    _, created = EntityInformation.objects.update_or_create(
            entity_number=e_num, defaults=e_obj
    )
    UPDATED_BENS.append(e_num)
    logger.warning(f'BEN: {e_num} ({e_obj["entity_name"]}) -> {_.id} ({_}) - Created: {created}')
    if e.parent_entities:
        for p_ben in e.parent_entities:
            if p_ben[0] not in UPDATED_BENS:
                logger.warning(f'Add/Update Parent: {p_ben[0]} - {p_ben[1]}')
                _p, created = EntityInformation.objects.update_or_create(
                    entity_number=p_ben[0], defaults={'entity_name': p_ben[1]}
                )
            p_obj = EntityInformation.objects.get(entity_number=p_ben[0])
            _.parent_entities.add(p_obj)
            
    if e.child_entities:
        for c_ben in e.child_entities:
            if c_ben[0] not in UPDATED_BENS:
                logger.warning(f'Add/Update Child: {c_ben[0]} - {c_ben[1]}')
                add_or_update_entity(c_ben[0])
            c_obj = EntityInformation.objects.get(entity_number=c_ben[0])
            _.child_entities.add(c_obj)
    

class Command(BaseCommand):
    def handle(self, **options):
        billed_entity_numbers_to_download = [
            '16076022',
            '143222',
            '143220',
        ]
        for ben in billed_entity_numbers_to_download:
            add_or_update_entity(ben)
