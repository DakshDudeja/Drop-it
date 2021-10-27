from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('update_active_bidding_orders/', views.update_active_bidding_orders, name="update_time"),
    path('get_all_auctions/', views.get_all_auctions, name="get_all_aucions"),
    path('get_auction/<str:pk>/', views.get_auction, name="get_auction"),
    path('update_auction/<str:pk>/', views.update_auction, name="update_auction"),
    path('post_auction/', views.post_auction, name="post_auction"),
    path('get_auction_bidder/<str:pk>/', views.get_auction_bidder, name="get_auction_bidder"),
   
    path('get_all_bids/', views.get_all_bids, name="get_bids"),
    path('get_bid/<str:pk>/', views.get_bid, name="get_bid"),
    path('update_bid/<str:pk>/', views.update_bid, name="update_bid"),
    path('post_bid/', views.post_bid, name="post_bid"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


