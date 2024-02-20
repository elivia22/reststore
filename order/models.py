from django.db import models


class Order(models.Model):
    class Meta:
        db_table = 'order'

    order_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    order_product_id = models.IntegerField()
    order_invoice_id = models.IntegerField()
    order_quantity = models.FloatField()
    order_unit_price = models.FloatField()
    order_total_price = models.FloatField()
    order_description = models.CharField(max_length=20)
