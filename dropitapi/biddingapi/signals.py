from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import *

class BiddingActions():
    auction = None
    def __init__(self, instance):
        self.auction = instance

    def update_auction(self):
        auction = self.auction
        auction.bid_count = Bid.BidManager.current(auction).count()
        auction.current_bid = format(auction.value, ".2f")
        auction.save()
        

@receiver(post_save, sender=Bid)
def update_auction_totals_for_bid(sender, instance, created, **kwargs):
    if created:
        auction = instance.auction
        auction.bid_count = Bid.BidManager.current(auction).count()
        auction.current_bid = instance.value
        auction.save()