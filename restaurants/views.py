from django.shortcuts import render, redirect
from .models import Restaurant
from .models import Item
from .models import Favorite

from .forms import RestaurantForm, UserRegisterForm, LoginForm, ItemForm
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse , HttpResponse

# Create your views here.
def user_login(request):
	form = LoginForm()
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			my_username = form.cleaned_data['username']
			my_password = form.cleaned_data['password']
			auth_user = authenticate(username=my_username, password=my_password)
			if auth_user is not None:
				login(request, auth_user)
				return redirect("restaurant_list")
	context = {
	"form":form

	}
	return render(request, 'login.html', context)
def user_register(request):
	form = UserRegisterForm()
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
	if form.is_valid():
			person =form.save(commit=False)
			person.set_password(person.password)
			person.save()
			login(request, person)
			return redirect("restaurant_list")

	context = {
		"form":form,
	}
	return render(request, 'register.html' , context)

def user_logout(request):
	logout(request)
	return redirect ('login')


def  list(request):
	if request.user.is_anonymous:
		return redirect("login")
	favorited_restaurants = []
	favorites = request.user.favorite_set.all()
	for favorite in favorites:
		favorited_restaurants.append(favorite.restaurant)

	context = {
		"restaurants": Restaurant.objects.all(),
		"my_favorites": favorited_restaurants
	}


	return render(request, 'list_view.html', context)

def  detail(request, restaurant_id):
	info = {
		"detail": Restaurant.objects.get(id=restaurant_id),
	}
	return render(request, 'detail_view.html', info)

def create(request):

	if request.user.is_anonymous:
		return redirect("login")

	form = RestaurantForm()
	if request.method == "POST":
		form = RestaurantForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect("restaurant_list")
	context = {
		"create_form":form,
	}
	return render(request, 'restaurant_create.html' , context)

def create_item(request, restaurant_id):
	form = ItemForm()
	rest = Restaurant.objects.get(id=restaurant_id)
	if request.method == "POST":
		form = ItemForm(request.POST, request.FILES or None)
		if form.is_valid():
			item_obj = form.save(commit=False)
			item_obj.restaurant = rest.id
			item_obj.save()
			return redirect("restaurant_list")
	context = {
		"form" :form,
		"restaurant": rest,
	}
	return render(request, 'create_item.html', context)
	
def update(request, restaurant_id):
	restaurant_obj =Restaurant.objects.get(id=restaurant_id)
	if not (request.user.is_staff or request.user==restaurant_obj.owner):
		return HttpResponse("<h1>You CAN'T UPDATE!)</h1>")

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
	if not (request.user.is_staff ):
		return HttpResponse("<h1>You CAN'T DELETE!)</h1>")
	instance = Restaurant.objects.get(id=restaurant_id)
	instance.delete()
	return redirect("restaurant_list")	

def favorite(request, restaurant_id):
	restaurant_obj = Restaurant.objects.get(id=restaurant_id)

	favorite_obj, created = Favorite.objects.get_or_create(user=request.user, restaurant=restaurant_obj)

	if created:
		action="favorite"
	else:
		action="unfavorite"
		favorite_obj.delete()

	favorite_count = restaurant_obj.favorite_set.all().count()

	context = {
	"action":action,
	"count":favorite_count,
	}

	return JsonResponse(context, safe=False)
