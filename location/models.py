from django.db import models


class Location(models.Model):
    class Meta:
        db_table = 'location'

    location_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    location_district = models.CharField(max_length=20)
    location_ward = models.CharField(max_length=20)
