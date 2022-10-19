from django.db.models import *
from django.contrib.auth.models import *
# Create your models here.
class CustomUser(AbstractUser):
    call_number = CharField(max_length=20)