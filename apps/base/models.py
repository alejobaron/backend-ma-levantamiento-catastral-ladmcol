from django.db import models

from simple_history.models import HistoricalRecords

# Create your models here.
class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creación', auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificación', auto_now=True)
    deleted_date = models.DateField('Fecha de Eliminación', null=True, blank=True)
    historical = HistoricalRecords(user_model="users.User", inherit = True)

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Bases'