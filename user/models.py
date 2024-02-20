from django.db import models


class User(models.Model):
    # class Meta:
        # db_table = 'auth_user'

    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    username = models.CharField(max_length=20)



