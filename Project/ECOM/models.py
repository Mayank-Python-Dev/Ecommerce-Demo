from django.db import models

# Create your models here.



class Customer(models.Model):
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	address = models.TextField(max_length=200,null=True)
	date = models.DateTimeField(auto_now_add=True,null=True)


	def __str__(self):
		return self.name



class Products(models.Model):
	options = (
		('Electronics','Electronics'),
		('Clothing','Clothing'),
		)

	name = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images')
	description = models.TextField(null=True,blank=True)
	price = models.IntegerField()
	category = models.CharField(max_length=100,choices = options,null=True)


	def __str__(self):
		return self.name



class Order(models.Model):
	order_status = (
		('Out for Delivery','Out for Delivery'),
		('Delivered','Delivered'),
		)
	customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,null=True,blank=True)
	product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,blank=True)
	quantity = models.IntegerField(null=True,blank=True)
	status = models.CharField(max_length=100,choices = order_status,null=True)
	price = models.IntegerField(null=True,blank=True)
	date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.status


class Transaction(models.Model):
    name=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    zip_code=models.CharField(max_length=500)
    phone=models.CharField(max_length=500, default="")
    amount=models.IntegerField(default=0)

    def __str__(self):
    	return self.name