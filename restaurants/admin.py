from django.contrib import admin
from .models import Restaurant
from .models import Item
from .models import Favorite
from .models import Favorite_item

admin.site.register(Restaurant)
admin.site.register(Item)
admin.site.register(Favorite)
admin.site.register(Favorite_item)

# Register your models here.
