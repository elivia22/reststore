from django.db import models


class Product(models.Model):
    class Meta:
        db_table = 'product'

    product_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_unit = models.FloatField()
    product_balance = models.FloatField()
    product_description = models.CharField(max_length=2083)
    # product_created_date = models.DateTimeField(auto_now_add=False)
    product_created_date = models.DateTimeField(auto_now_add=True)
    product_created_by = models.CharField(max_length=50)



