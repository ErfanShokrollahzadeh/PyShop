from django.db import models


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    discount = models.FloatField()

class Home(models.Model):
    objects = None
    img_url = models.CharField(max_length=2083)

class image(models.Model):
    objects = None
    img_url = models.CharField(max_length=2083)

class Signup(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Login(models.Model):
    objects = None
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Comment(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Notexits(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

