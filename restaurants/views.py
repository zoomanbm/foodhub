from django.shortcuts import render, redirect
from .models import Restaurant
from .models import Detail_Restaurant
from .forms import RestaurantForm

# Create your views here.
def  list(request):
	context = {
		"restaurants": Restaurant.objects.all(),
	}
	return render(request, 'list_view.html', context)

def  detail(request, restaurant_id):
	info = {
		"detail": Restaurant.objects.get(id=restaurant_id),
	}
	return render(request, 'detail_view.html', info)

def create(request):
	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("restaurant_list")
	context = {
		"create_form":form,
	}
	return render(request, 'restaurant_create.html' , context)

def update(request, restaurant_id):
	restaurant_obj =Restaurant.objects.get(id=restaurant_id)
	form = RestaurantForm(request.POST, instance=restaurant_obj)
	if request.method == "POST":
		form = RestaurantForm(request.POST, instance=restaurant_obj)
		if form.is_valid():
			form.save()
			return redirect("restaurant_list")
	context = {
	"restaurant_obj":restaurant_obj,
	"update_form":form,

	}
	return render(request, 'restaurant_update.html', context)
def restaurant_delete (request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    instance.delete()
    return redirect("restaurant_list")	
