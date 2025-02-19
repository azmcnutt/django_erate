from django.db import models

# Create your models here.
class EntityInformation(models.Model):
    entity_name = models.CharField(
        verbose_name='Entity Name',
        max_length=64,
        null=True,
        blank=True,
        unique=False,
    )
    entity_number = models.CharField(
        verbose_name='Entity Number',
        max_length=32,
        null=False,
        blank=False,
        unique=True,
    )
    entity_type = models.CharField(
        verbose_name='Entity Type',
        max_length=16,
        null=True,
        blank=True,
        unique=False,
    )
    parent_entities = models.ManyToManyField(
        'EntityInformation',
        related_name='parents',
        blank=True,
        unique=False,
    )
    child_entities = models.ManyToManyField(
        'EntityInformation',
        related_name='children',
        blank=True,
        unique=False,
    )

    class Meta:
        ordering = ('entity_number',)
        verbose_name = 'Billed Entity'
        verbose_name_plural = 'Billed Entities'
    
    def __str__ (self):
        return str(self.entity_number)