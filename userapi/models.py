from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save

#All costumer/dropper registraion model with fields as username, email, phone_number, first_name, last_name
class User(AbstractUser):
    username = models.CharField(blank = False, unique = True,max_length = 30)
    email = models.EmailField(unique = True, blank = True)
    phone_number = models.CharField(max_length = 10, unique = True, blank = False )
    REQUIRED_FIELDS  = ['first_name', 'email', 'phone_number']

    def __str__(self):
        return '{}'.format(self.username)


#User/coustomer profile model with fields as user_age, user_profile_photo along with user model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'profile')
    user_age = models.IntegerField(null=False)
    user_profile_photo = models.URLField(blank = True)
    user_gender = models.CharField(max_length=8, null=True)
    is_dropper = models.BooleanField(default=False)
    def __str__(self):
        return '{}'.format(self.user.username)


# To trigger userprofile model to create instant profile as dropper gets registereed
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_or_save_user_profile(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
    instance.profile.save()


#dropper profile model with fields as dropper_age, droper_gender, dropper_profile_photo, dropper_authentication_number
#dropper_authentication_photo, dropper_vehicle_type, dropper_rc_photo, dropper_driving_liscence_photo
class DropperProfile(models.Model):
    dropper = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'dropper')
    dropper_age = models.IntegerField(null=False)
    dropper_gender = models.CharField(max_length=8, null=True)
    dropper_profile_photo = models.URLField(blank = True)
    dropper_authentication_number = models.IntegerField(null=False)
    dropper_authentication_photo = models.URLField( blank = False) 
    dropper_vehicle_type = models.CharField(max_length = 10, blank = False )
    dropper_rc_photo = models.URLField(blank = False)
    dropper_driving_liscence_photo = models.URLField(blank = False)
    def __str__(self):
        return '{}'.format(self.dropper.username)


# To trigger dropper profile model to create instant profile as dropper gets registereed
@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def create_or_save_dropper_profile(sender, created, instance, **kwargs):
    if created:
        DropperProfile.objects.create(dropper = instance)
    instance.profile.save()

class DropperRatingData(models.Model): 
    dropper_name= models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'dropper_name', primary_key=True)
    delivery_count = models.IntegerField(default=0)
    dropper_rating = models.DecimalField(default=0, decimal_places=2,max_digits=10)
    total_distance_covered = models.DecimalField(default=0, decimal_places=2,max_digits=10)
    total_earnings = models.IntegerField(default = 0 )
    total_time_on_road =  models.IntegerField(default=0)
    def __str__(self):
        return '{}'.format(self.dropper_name.username)


@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def Dropper_rating_data(sender, created, instance, **kwargs):
    if created:
        DropperRatingData.objects.create(dropper_name = instance)
    instance.profile.save()



class OrdersModel(models.Model):
    parcel_choices = (
                     ("Food","Food"),
                     ("Documents","Documents"),
                     ("Electronics","Electronics"),
                     ("Small_furniture","Small_furniture"),
                     ("others","others"))

    weight_choices = (
                     ("under_5kg","under_5kg"),
                     ("under_10kg","under_10kg"),
                     ("under_20kg","under_20kg"),
                     ("under_30kg","under_30kg"),
                     ("Above_30kg","Above_30kg"))

    size_choices = (
                     ("fits_in_small_bag","fits_in_small_bag"),
                     ("Fits_in_car","Fits_in_car"),
                     ("Fit_In_truck","Fit_In_truck"))

    payment_method_choices = (
                     ("UPI","UPI"),
                     ("Net_Banking","Net_Banking"),
                     ("Cash_on_delivery","Cash_on_delivery"))
                     
    user_of_order = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'user_of_order')
    pickup_location = models.CharField(null = False, max_length = 150)
    pickup_landmark = models.CharField(null = True, max_length = 50)
    pickup_phone_number = models.CharField(null = False, max_length = 13)
    drop_location = models.CharField(null = False, max_length = 50)
    drop_landmark = models.CharField(null = True, max_length = 150)
    drop_phone_number = models.CharField(null = False, max_length = 13)
    parcel_image = models.URLField(blank = True)
    parcel_category = models.CharField(max_length = 20, default = 'parcel', choices = parcel_choices)
    weight_category = models.CharField(max_length = 20, default = '10kg', choices = weight_choices)
    size_category = models.CharField(max_length = 20, default = '50cm', choices = size_choices)
    payment_method = models.CharField(max_length = 20, default = 'UPI', choices = payment_method_choices)
    def __str__(self):
        return '{}'.format(self.user_of_order)


#######################################################################################################################
