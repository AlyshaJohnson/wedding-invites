from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import googlemaps
import json
from wedding_invite import settings

STATUS = ((0, "Draft"), (1, "Published"))
YES_NO = ((0, "No"), (1, "Yes"))


class Guest(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)  # noqa
    first_name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=50, unique=False)
    status = models.IntegerField(choices=STATUS, default=0)
    email = models.CharField(max_length=100, unique=False)
    phone = models.CharField(max_length=100, unique=False, blank=True)
    RSVP = models.BooleanField(blank=True, null=True)
    RSVP_comment = models.CharField(max_length=200, unique=False, blank=True)
    hotel = models.CharField(max_length=200, unique=False, blank=True)
    party_admin = models.IntegerField(choices=YES_NO, default=0)
    linked_party = models.ManyToManyField(
        "self",
        related_name="party_admin",
        blank=True,
        symmetrical=True
    )

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


class Wedding(models.Model):
    couple = models.ManyToManyField(
        "Guest",
        blank=False,
    )
    wedding_date = models.DateField(auto_now=False, blank=True, null=True)
    venue1 = models.CharField(max_length=100, unique=False, blank=True)
    venue1_time = models.TimeField(auto_now=False, blank=True, null=True)
    venue1_address = models.TextField(blank=True)
    venue1_lat = models.TextField(blank=True)
    venue1_lon = models.TextField(blank=True)
    venue2 = models.CharField(max_length=100, unique=False, blank=True)
    venue2_time = models.TimeField(auto_now=False, blank=True, null=True)
    venue2_address = models.TextField(blank=True)
    venue2_lat = models.TextField(blank=True)
    venue2_lon = models.TextField(blank=True)
    rsvp_date = models.DateTimeField(auto_now=False, blank=True, null=True)
    menu = CloudinaryField('image', blank=True)
    starter1 = models.CharField(max_length=200, unique=False, blank=True)
    starter1_ingredients = models.TextField(blank=True)
    starter2 = models.CharField(max_length=200, unique=False, blank=True)
    starter2_ingredients = models.TextField(blank=True)
    starter3 = models.CharField(max_length=200, unique=False, blank=True)
    starter3_ingredients = models.TextField(blank=True)
    main1 = models.CharField(max_length=200, unique=False, blank=True)
    main1_ingredients = models.TextField(blank=True)
    main2 = models.CharField(max_length=200, unique=False, blank=True)
    main2_ingredients = models.TextField(blank=True)
    main3 = models.CharField(max_length=200, unique=False, blank=True)
    main3_ingredients = models.TextField(blank=True)
    dessert1 = models.CharField(max_length=200, unique=False, blank=True)
    dessert1_ingredients = models.TextField(blank=True)
    dessert2 = models.CharField(max_length=200, unique=False, blank=True)
    dessert2_ingredients = models.TextField(blank=True)
    dessert3 = models.CharField(max_length=200, unique=False, blank=True)
    dessert3_ingredients = models.TextField(blank=True)
    other_info = models.TextField(max_length=200, unique=False, blank=True)
    active = models.BooleanField(default=False)

    def get_lat_lon(address):
        gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
        get_address = json.dumps(gmaps.geocode(address))
        result = json.loads(get_address)
        latitude = result[0]['geometry']['location']['lat']
        longitude = result[0]['geometry']['location']['lng']
        return (latitude, longitude)

    def save(self, *args, **kwargs):
        if self.venue1_address != "":
            self.venue1_lat = Wedding.get_lat_lon(self.venue1_address)[0]
            self.venue1_lon = Wedding.get_lat_lon(self.venue1_address)[1]
            super(Wedding, self).save(*args, **kwargs)
        if self.venue2_address != "":
            self.venue2_lat = Wedding.get_lat_lon(self.venue2_address)[0]
            self.venue2_lon = Wedding.get_lat_lon(self.venue2_address)[1]
            super(Wedding, self).save(*args, **kwargs)


class Food(models.Model):
    active_wedding = Wedding.objects.filter(active=True).first()
    STARTER_CHOICES = [
        ('starter1', active_wedding.starter1),
        ('starter2', active_wedding.starter2),
        ('starter3', active_wedding.starter3)
    ]

    MAIN_CHOICES = [
        ('main1', active_wedding.main1),
        ('main2', active_wedding.main2),
        ('main3', active_wedding.main3)
    ]

    DESSERT_CHOICES = [
        ('dessert1', active_wedding.dessert1),
        ('dessert2', active_wedding.dessert2),
        ('dessert3', active_wedding.dessert3)
    ]
    guest_id = models.OneToOneField(Guest, on_delete=models.CASCADE, unique=True)  # noqa
    starter = models.CharField(
        max_length=200,
        unique=False,
        choices=STARTER_CHOICES,
        default=None
    )
    main = models.CharField(
        max_length=200,
        unique=False,
        choices=MAIN_CHOICES,
        default=None
    )
    dessert = models.CharField(
        max_length=200,
        unique=False,
        choices=DESSERT_CHOICES,
        default=None
    )
    allergies = models.CharField(max_length=100, unique=False, blank=True)
    diet = models.CharField(max_length=100, unique=False, blank=True)

    def __str__(self):
        return f"{self.guest_id.first_name}, {self.guest_id.last_name}"


class Song(models.Model):
    song = models.CharField(max_length=100, unique=False)
    artist = models.CharField(max_length=100, unique=False)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-song"]

    def __str__(self):
        return f"{self.song}, {self.artist}"


class Hotel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.TextField()
    website = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Image(models.Model):
    description = models.TextField(blank=True)
    file = CloudinaryField('image')
    date_added = models.DateField(auto_now=True)
    order = models.IntegerField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.order = 1
        while True:
            number = Image.objects.filter(order=self.order)
            if not number:
                break
            else:
                self.order += 1
        super(Image, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-order"]

    def __str__(self):
        return f"{self.file}, {self.date_added}"


class Message(models.Model):
    guest_id = models.ForeignKey(Guest, on_delete=models.PROTECT)
    title = models.CharField(max_length=200, unique=False)
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    date_sent = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.date_sent}"
