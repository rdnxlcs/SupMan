from django.db import models
class Points(models.Model):
  idx = models.IntegerField(unique=True)
  name = models.CharField(default="", max_length = 128)

class Items(models.Model):
  idx = models.IntegerField(unique=True)
  category = models.CharField(default="", max_length = 128)
  name = models.CharField(default="", max_length = 128)
  unit = models.CharField(default="", max_length = 16)
  rule = models.IntegerField()
  quantity = models.IntegerField(default=0)
  to_supply = models.IntegerField(default=0)
  supplier = models.CharField(default="", max_length = 128)
  point = models.CharField(default="", max_length = 128)
  def __str__(self) -> str:
    return f'{self.name}'