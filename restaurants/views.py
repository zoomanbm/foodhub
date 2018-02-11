from django.shortcuts import render

# Create your views here.
def  list(request):
	context = {
		"restaurants":[
		{
		"Name": "MR.Zee's",
		"content": "American Diner",
		"created": "2018--02-07",
		"updated": "2018--02-08",
		},
		{
		"Name": "MR.Bee's",
		"content": "Indian Diner",
		"created": "2018--02-07",
		"updated": "2018--02-08",
		},
		{
		"Name": "MR.A's",
		"content": "Jamaican Diner",
		"created": "2018--02-07",
		"updated": "2018--02-08",
		},
		{
		"Name": "MR.D's",
		"content": "Italian Diner",
		"created": "2018--02-07",
		"updated": "2018--02-08",
		},
		]
	}
	return render(request, 'detail_view.html', context)
