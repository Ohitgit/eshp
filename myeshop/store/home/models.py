from django.db import models

# Create your models here.
class Category(models.Model):
      categoryname=models.CharField(max_length=50,null=True)
      def __str__(self):
            return self.categoryname

class Product(models.Model):
      name=models.CharField(max_length=50,null=True)
      def __str__(self):
            return self.name
class Notes(models.Model):
      cat=models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
      pro=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
      notes=models.CharField(max_length=50,null=True)
      description=models.TextField(max_length=100,null=True)

class Country(models.Model):
      name=models.CharField(max_length=50,null=True)

      def __str__(self):
            return self.name

class State(models.Model):
      Country=models.ForeignKey(Country,on_delete=models.CASCADE,null=True)
      name=models.CharField(max_length=50,null=True)

      def __str__(self):
            return self.name


class District(models.Model):
      state=models.ForeignKey(State,on_delete=models.CASCADE,null=True)
      name=models.CharField(max_length=50,null=True)
