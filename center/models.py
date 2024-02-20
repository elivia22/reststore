from django.db import models


class Center(models.Model):
    class Meta:
        db_table = 'center'

    center_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    center_name = models.CharField(max_length=20)
    center_location_id = models.IntegerField()
