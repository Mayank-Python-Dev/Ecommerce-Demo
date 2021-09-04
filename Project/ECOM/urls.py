from django.urls import path

from .import views

urlpatterns = [

	path('',views.index,name='home'),

	path('product_detail/<str:pk>/',views.detail,name = 'product_detail'),

	path('cart/<str:pk>/',views.order,name = 'cart'),

	path('update_order/<str:pk>',views.editOrder,name = 'updateOrder'),

	path('delete_order/<str:pk>/',views.deleteOrder,name = 'deleteOrder'),

	path('total_details/',views.totalDetails,name = 'totaldetails'),

	path('create_customer/',views.createCustomer,name = 'customer_dashboard'),

	path('update_customer/<str:pk>/',views.editCustomer,name = 'updateCustomer'),
	
	path('delete_customer/<str:pk>',views.deleteCustomer,name ='deleteCustomer'),

	path('create_products/',views.createProducts, name = 'product_dashboard'),

	path('update_products/<str:pk>/',views.editProducts,name = 'updateProducts'),

	path('delete_products/<str:pk>/',views.deleteProducts, name = 'deleteProducts'),

	#PAYMENT

	# path('payment/<str:pk>',views.Payment, name = 'payment'),

	# path('payment_complete',views.paymentComplete,name = 'payment_complete')

	#PAYTM

	path('make_payment/<int:pk>/',views.Paytm,name = 'paytm'),

	path('handle_request/',views.handlePaytmRequest,name = 'handle_request'),

]