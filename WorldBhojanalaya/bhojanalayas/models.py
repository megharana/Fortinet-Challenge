from django.db import models
from django.conf import settings


class Details(models.Model):
    resturant_id = models.CharField(max_length=10, primary_key=True)
    rest_name = models.CharField(max_length=100)
    cuisines = models.CharField(max_length=100)
    avg_cost_ofTwo = models.IntegerField()
    currency = models.CharField(max_length=50)
    has_table_booking = models.CharField(max_length=4)
    has_online_delivery = models.CharField(max_length=4)
    aggregate_rating = models.FloatField()
    rating_color = models.CharField(max_length=40)
    rating_text = models.CharField(max_length=30)
    votes = models.IntegerField()


class Address(models.Model):
    rest_id = models.ForeignKey(Details, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    locality = models.CharField(max_length=100)
    locality_verbose = models.CharField(max_length=150)
    longitude = models.FloatField()
    latitude = models.FloatField()
