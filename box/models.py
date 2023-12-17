from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Box(models.Model):
  id=models.AutoField(primary_key=True,editable=False)
  creator=models.ForeignKey(User,on_delete=models.PROTECT)
  length=models.FloatField(default=1)
  breadth=models.FloatField(default=1)
  height=models.FloatField(default=1)
  area=models.FloatField(default=1)
  volume=models.FloatField(default=1)
  created_by=models.DateTimeField(auto_now_add=True)
  updated_by=models.DateField(auto_now=True)
  

  def __str__(self):
      return self.creator.username
  class Meta:
    verbose_name_plural="Boxes"

  def save(self,*args, **kwargs):
    self.area =2*(self.length*self.breadth+self.breadth*self.height+self.height*self.length)
    self.volume= (self.length*self.breadth*self.height)
    super().save(*args,**kwargs)
