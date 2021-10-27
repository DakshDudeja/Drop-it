from .models import Auction, Bid
from datetime import datetime, timedelta
from rest_framework import viewsets, status
from .serializers import BidSerializer, AuctionSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.shortcuts import render
from django.views.decorators.cache import never_cache

# Create your views here.
def update_active_bidding_orders(request):
    current_time = datetime.now().time()
    current_date = datetime.now().date()
    expired_bid_ids = Auction.objects.all()
    for val in expired_bid_ids:
        if val.expiry_date.time() < current_time and val.expiry_date.date() < current_date:
            val.active =False
            val.save()
            return 0
##############################################################################################################################

@api_view(['GET'])
@never_cache
def get_all_auctions(request):
    if request.method == 'GET':
        auction = Auction.objects.all()
        serializer = AuctionSerializer(auction,many = True)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
@never_cache
def post_auction(request):
     if request.method == 'POST':
        serializer  = AuctionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
@never_cache
def get_auction(request, pk):
    auction = Auction.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = AuctionSerializer(auction)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT', 'DELETE' ])
@never_cache
def update_auction(request, pk):
    auction = Auction.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = AuctionSerializer(auction)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = AuctionSerializer(auction, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        auction.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@never_cache
def get_all_bids(request):
    if request.method == 'GET':
        bid = Bid.objects.all()
        serializer = BidSerializer(bid,many = True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer  = BidSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['POST'])
@never_cache
def post_bid(request):
     if request.method == 'POST':
        serializer  = BidSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
@never_cache
def get_bid(request, pk):
    bid = Bid.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = BidSerializer(bid)
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
@never_cache
def update_bid(request, pk):
    bid = Bid.objects.get(pk = pk)
    if request.method == 'GET':
        serializer = BidSerializer(bid)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = BidSerializer(bid, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        bid.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'DELETE'])
@never_cache
def get_auction_bidder(request, pk):
    if request.method == 'GET':
        all_bidders = Bid.objects.all()
        temp = {}
        for bid in all_bidders:
            if(str(bid.auction.pk)==pk):
                serializer = BidSerializer(bid)
                temp[str(bid.pk)] = serializer.data
        
        return Response(temp)
    else:
        return Response(serializer.errors)
