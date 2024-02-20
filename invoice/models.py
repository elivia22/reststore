from django.db import models


class Invoice(models.Model):
    class Meta:
        db_table = 'invoice'

    invoice_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    invoice_datetime = models.DateTimeField(auto_now_add=True)
    invoice_amount = models.FloatField()
    invoice_center_id = models.IntegerField()
    invoice_created_by = models.CharField(max_length=50)

