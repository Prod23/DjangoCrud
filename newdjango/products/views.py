from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from .forms import RawProductForm
# Create your views here.

def dynamic_lookup_view(request,my_id):
	obj = Product.objects.get(id = my_id)
	if request.method == "POST":
		obj.delete()
	context = {
		"object" : obj
	}
	return render(request,"product/product_detail.html",context)


def product_list(request):
	queryset = Product.objects.all()

	context = {
		"object_list": queryset
	}
	return render(request,"product/product_detail.html",context)


def product_create_view(request):
	my_form = RawProductForm()
	if request.method == "POST":
		my_form = RawProductForm(request.POST)
		if my_form.is_valid():
			print(my_form.cleaned_data)
			Product.objects.create(**my_form.cleaned_data)
	context = {
		"form": my_form
	}
	return render(request,"product/product_create.html",context)



def product_detail_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()
	context={
		'form' : form
	}
	return render(request,"product/product_detail.html",context)