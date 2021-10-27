from django.contrib import admin

# Register your models here.
from .models import UserProfile, User, DropperProfile, OrdersModel,DropperRatingData
admin.site.register(UserProfile)
admin.site.register(DropperProfile)
admin.site.register(User)
admin.site.register(OrdersModel)
admin.site.register(DropperRatingData)
