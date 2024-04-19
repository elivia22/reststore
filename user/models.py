from django.db import models


class User(models.Model):
    # class Meta:
    #     db_table = 'auth_user'

    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    # password2 = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    is_superuser = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_staff = models.CharField(max_length=20)
    is_active = models.CharField(max_length=20)
    date_joined = models.CharField(max_length=20)






