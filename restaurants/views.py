from django.shortcuts import render
from .models import Restaurant
from .models import Detail_Restaurant

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