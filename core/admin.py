from django.contrib import admin
from core.models import EntityInformation

class SaveAsAdmin(admin.ModelAdmin):
    save_as = True

# Register your models here.

class EntityInformationAdmin(admin.ModelAdmin):
    list_display = ('entity_number','entity_name','entity_type',)
    list_filter = ('entity_type',)
    search_fields = ('entity_number','entity_name','entity_type','parent_entities__entity_number','child_entities__entity_number',)
    ordering = ('entity_number',)


admin.site.register(EntityInformation, EntityInformationAdmin)