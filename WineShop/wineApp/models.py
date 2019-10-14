from django.db import models


class Wine(models.Model):
    country = models.CharField(max_length=100, null=True, default='')
    description = models.CharField(max_length=2500, null=True, default='')
    designation = models.CharField(max_length=100, null=True, default='')
    points = models.IntegerField(null=True, default=0)
    price = models.FloatField(null=True, default=0.0)
    province = models.CharField(max_length=100, null=True, default='')
    region_1 = models.CharField(max_length=100, null=True, default='')
    region_2 = models.CharField(max_length=100, null=True, default='')
    variety = models.CharField(max_length=100, null=True, default='')
    winery = models.CharField(max_length=100, null=True, default='')

    def __str__(self):
        return self.designation

