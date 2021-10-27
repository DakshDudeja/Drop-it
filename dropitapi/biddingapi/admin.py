from django.contrib import admin
from .models import *

# class AuctionAdmin(admin.ModelAdmin):
#     list_display = ['title', 'base_fare_display','created_at', 'expiry_date', 'active']

#     def base_fare_display(self, obj):
#         return "£{0}".format(obj.basic_fare)


# class BidAdmin(admin.ModelAdmin):
#     list_display = ['value', 'owner', 'created_at']


admin.site.register(Auction)
admin.site.register(Bid)
