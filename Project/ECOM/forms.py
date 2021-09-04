from django import forms

from .models import *

class OrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['customer','quantity','status']


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'



class ProductsForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = '__all__'


class TransactionForm(forms.ModelForm):
	class Meta:
		model = Transaction
		exclude = ['amount']