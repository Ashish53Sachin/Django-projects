from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices

# id = models.BigAutoField(primary_key=True

# fname = models.CharField(max_length=50)
# lname = models.CharField(max_length=50)
# age = models.IntegerField(default=0, null=True)
# email = models.EmailField()
# gender = models.CharField(max_length=1, choices=GENDER, )
    # class Meta:
    #     db_table="person"


# Create your models here.

# Create your models here.
class Person(models.Model):
    GENDER = Choices(
        (1, "male", _("male")),
        (2, "female", _("female")),
        (3, "others", _("others")),
    )
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField()
    email= models.EmailField()
    gender = models.IntegerField(choices=GENDER, default=GENDER.male)
    #random changes
    # class Meta:
    #     db_table="person"