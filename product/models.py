from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    category = models.ForeignKey(Category)
    grade = models.ForeignKey(Grade)
    author = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)
    code = models.CharField(max_length=250, unique=True)
    price = models.IntegerField(null=True, blank=True)
    amout = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name
