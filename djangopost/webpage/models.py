from django.db import models
from django.utils import timezone
# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True)
    time = models.DateTimeField(default=timezone.now)


    def __str__(self): #미들웨어한테 정보 알려주기위해 어드민 Person 그룹에 이름을 보이게함
        return "%s%s %d " % (self.last_name,self.first_name, self.age)