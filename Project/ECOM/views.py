from django.shortcuts import render,redirect

from .models import *

from .forms import *

from django.contrib import messages

# Create your views here.


def index(request):
	getAllProduct = Products.objects.all()
	context = {'getAllProduct' : getAllProduct}
	return render(request,'ECOM/index.html',context)


def detail(request,pk):
	getProduct = Products.objects.get(id = pk)
	context = {'getProduct':getProduct}
	return render(request,'ECOM/product_detail.html',context)


def order(request,pk):
	getProductID = Products.objects.get(id=pk)
	getPerOrderWithProductID = Order.objects.filter(product_id = getProductID).all()
	form  = OrderForm()
	if request.method == "POST":
		form = OrderForm(request.POST)
		getForm = form.save(commit=True)
		getForm.product = getProductID
		getForm.price = getProductID.price * int(request.POST.get('quantity'))
		getForm.save()
		messages.success(request, 'ORDER CREATED!')
		return redirect('cart' ,getProductID.id)
	context = {'form':form,'getProductID':getProductID,'getPerOrderWithProductID':getPerOrderWithProductID}
	return render(request,'ECOM/cart_form.html',context)


def getTotalOrder(request):
	return render(request,'ECOM/total_order_detail.html')



def editOrder(request,pk):
	form = OrderForm()
	getOrderID = Order.objects.get(id=pk)
	form = OrderForm(instance = getOrderID)
	if request.method == "POST":
		form = OrderForm(request.POST,instance = getOrderID)
		if form.is_valid():
			getForm = form.save(commit=True)
			getForm.quantity = int(request.POST.get('quantity'))
			getForm.price = int(request.POST.get('quantity')) * getOrderID.product.price
			getForm.status = request.POST.get('status')
			getForm.save()
			return redirect('cart',getOrderID.product.id)

	context = {'form':form}
	return render(request,'ECOM/edit_order.html',context)


def deleteOrder(request,pk):
	getOrder = Order.objects.get(id=pk)
	getOrder.delete()
	messages.success(request,'ORDERED DELETED!')
	return redirect('cart',getOrder.product.id)


def totalDetails(request):
	getAllCustomer = Customer.objects.all().count()
	getTotalOrder = Order.objects.all().count()
	getTotalProduct = Products.objects.all().count()
	getTotalDelivered = Order.objects.filter(status = 'Delivered').count()
	context = {'getTotalOrder':getTotalOrder,'getAllCustomer':getAllCustomer,'getTotalProduct':getTotalProduct,'getTotalDelivered':getTotalDelivered}
	return render(request,'ECOM/total_orders.html',context)


def createCustomer(request):
	getAllCustomer = Customer.objects.all()
	form = CustomerForm()
	if request.method == "POST":
		form = CustomerForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,'CUSTOMER CREATED!')
			return redirect('customer_dashboard')
	context = {'form':form,'getAllCustomer':getAllCustomer}
	return render(request,'ECOM/customer_dashboard.html',context)


def editCustomer(request,pk):
	form = CustomerForm()
	getCustomerID = Customer.objects.get(id=pk)
	form = CustomerForm(instance = getCustomerID)
	if request.method == "POST":
		form = CustomerForm(request.POST,instance = getCustomerID)
		if form.is_valid():
			form.save()
			messages.success(request,'CUSTOMER UPDATED!')
			return redirect('customer_dashboard')

	context = {'form':form}
	return render(request,'ECOM/edit_customer.html',context)


def deleteCustomer(request,pk):
	getCustomerID = Customer.objects.get(id=pk)
	getCustomerID.delete()
	messages.success(request,'CUSTOMER DELETED!')
	return redirect('customer_dashboard')



def createProducts(request):
	getAllProducts = Products.objects.all()
	form = ProductsForm()
	if request.method == "POST":
		form = ProductsForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request,'PRODUCT ADDED!')
			return redirect('product_dashboard')
	context = {'form':form,'getAllProducts' : getAllProducts}
	return render(request,'ECOM/product_dashboard.html',context)



def editProducts(request,pk):
	form = ProductsForm()
	getProductID = Products.objects.get(id=pk)
	form = ProductsForm(instance = getProductID)
	if request.method == "POST":
		form = ProductsForm(request.POST,request.FILES,instance = getProductID)
		if form.is_valid():
			form.save()
			messages.success(request,'PRODUCTS UPDATED!')
			return redirect('product_dashboard')
	context = {'form':form}
	return render(request,'ECOM/edit_product.html',context)


def deleteProducts(request,pk):
	getProductID = Products.objects.get(id=pk)
	getProductID.delete()
	messages.success(request,'PRODUCT DELETED!')
	return redirect('product_dashboard')