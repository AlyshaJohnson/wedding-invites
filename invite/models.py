from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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
    venue2 = models.CharField(max_length=100, unique=False, blank=True)
    venue2_time = models.TimeField(auto_now=False, blank=True, null=True)
    venue2_address = models.TextField(blank=True)
    menu = CloudinaryField(blank=True)
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

    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
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
    file = models.FileField()
    date_added = models.DateField(auto_now=True)
    order = models.IntegerField(unique=True)

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
