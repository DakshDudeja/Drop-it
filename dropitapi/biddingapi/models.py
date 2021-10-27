from django.db import models
from django.conf import settings
from datetime import datetime, timedelta
import time
# User = settings.AUTH_USER_MODEL
from userapi.models import User
class Auction(models.Model):
    title = models.CharField(max_length=255)
    basic_fare = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField()
    active = models.BooleanField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE)


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete = models.CASCADE)
    value = models.FloatField()
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)



# class AuctionManager(models.Manager):
#     def active(self):
#         return super().get_queryset().filter(active=True)

#     def expired(self):
#         return super().get_queryset().filter(active=False)


    # def __str__(self):
    #     return "{0}".format(self.owner)

    # objects = models.Manager()
    # BidManager = BidManager()

# class IsActiveManager(models.Manager):
#     def get_queryset(self):
#         return super(IsActiveManager, self).get_queryset().filter(active=True).order_by('-created_at')


# class BidManager(models.Manager):
#     def current(self, auction):
#         return super().get_queryset().filter(auction=auction).order_by('-created_at')

# class Board(models.Model):
#     characters = models.fields_all()