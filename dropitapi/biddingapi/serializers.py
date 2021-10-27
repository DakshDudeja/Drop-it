from .models import Bid, Auction
from rest_framework  import serializers
from django.contrib.auth import authenticate

class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = "__all__"


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = "__all__"

