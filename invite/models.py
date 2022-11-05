from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Guests(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    email = models.CharField(max_length=100, unique=False)
    phone = models.CharField(max_length=100, unique=False)
    RSVP = models.BooleanField(default=False)
    RSVP_comment = models.CharField(max_length=200, unique=False)
    hotel = models.CharField(max_length=200, unique=False)
    party_admin = models.ForeignKey('self', on_delete=models.PROTECT)


class Wedding(models.Model):
    to_be_wed = models.ForeignKey(Guests, on_delete=models.PROTECT)
    wedding_date = models.DateField(auto_now=False)
    venue1 = models.CharField(max_length=100, unique=False)
    venue1_time = models.TimeField(auto_now=False)
    venue1_address = models.TextField()
    venue2 = models.CharField(max_length=100, unique=False)
    venue2_time = models.TimeField(auto_now=False)
    venue2_address = models.TextField()
    menu = CloudinaryField()
    starter1 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    starter2 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    starter3 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    main1 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    main2 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    main3 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    dessert1 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    dessert2 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    dessert3 = models.CharField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()
    other_info = models.TextField(max_length=200, unique=False)
    starter1_ingredients = models.TextField()


class Food(models.Model):
    class StarterChoices(models.TextChoices):
        STARTER1 = Wedding.starter1
        STARTER2 = Wedding.starter2
        STARTER3 = Wedding.starter3

    class MainChoices(models.TextChoices):
        MAIN1 = Wedding.main1
        MAIN2 = Wedding.main2
        MAIN3 = Wedding.main3

    class DessertChoices(models.TextChoices):
        DESSERT1 = Wedding.dessert1
        DESSERT2 = Wedding.dessert2
        DESSERT3 = Wedding.dessert3

    guest_id = models.ForeignKey(Guests, on_delete=models.CASCADE)
    starter = models.CharField(
        max_length=200,
        unique=False,
        choices=StarterChoices.choices,
        default=None
    )
    main = models.CharField(
        max_length=200,
        unique=False,
        choices=MainChoices.choices,
        default=None
    )
    dessert = models.CharField(
        max_length=200,
        unique=False,
        choices=DessertChoices.choices,
        default=None
    )
    allergies = models.CharField(max_length=100, unique=False)
    diet = models.CharField(max_length=100, unique=False)


class Songs(models.Model):
    song = models.CharField(max_length=100, unique=False)
    artist = models.CharField(max_length=100, unique=False)
    guest = models.ForeignKey(Guests, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-song"]


class Hotels(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    website = models.CharField(max_length=100, unique=True)


class Images(models.Model):
    guest_id = models.ForeignKey(Guests, on_delete=models.PROTECT)
    description = models.TextField()
    date_added = models.DateField(auto_now=True)
    order = models.IntegerField(unique=True)


class Messages(models.Model):
    guest_id = models.ForeignKey(Guests, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, unique=False)
    description = models.TextField()
    date_created = models.DateField(auto_now=True)
    date_sent = models.DateField(auto_now=True)
