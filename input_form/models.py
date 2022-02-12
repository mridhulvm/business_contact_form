from django.db import models

from django.utils import timezone
# Create your models here.

class date(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class BusinessType(date):
    name = models.CharField(max_length=255,null = False, blank = False)

    def __str__(self):
        return self.name+" created_at  "+str(self.created_at)

class InputForm(date):
    name = models.CharField(max_length=255,null = False, blank = False)
    contact  = models.CharField(max_length=255,null = False, blank = False)
    business_type = models.ForeignKey(BusinessType,on_delete=models.CASCADE)
    contact_number  = models.IntegerField(null = False, blank = False)
    International_code = models.IntegerField(null = False, blank = False)

    def __str__(self):
        return self.name+" "+str(self.created_at)
