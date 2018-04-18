from __future__ import unicode_literals
from django.db import models

class ProductsManager(models.Manager):
	def validate(self, form_data):
		errors = []
		name = form_data['name']

		if len(name) == 0:
			errors.append("Please type product/item name")
		if len(name) < 3:
			errors.append("Product/Item name should be more than 3 characters long")

		return errors


class Products(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def __str__(self):
		return "description:{} name:{}".format(self.description, self.name)