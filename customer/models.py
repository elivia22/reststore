from django.db import models


class Customer(models.Model):
    class Meta:
        db_table = 'customer'

    customer_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_name = models.CharField(max_length=50)
    customer_location_id = models.IntegerField()
