from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from django_summernote.admin import SummernoteModelAdmin
from .models import Guest, Wedding, Food, Song, Hotel, Image, Message


admin.site.unregister(Group)


@admin.register(Guest)
class GuestAdmin(SummernoteModelAdmin):
    list_display = ("user_id", "first_name", "last_name", "status", "RSVP", "party_admin", "view_party")  # noqa

    def view_party(self, obj):
        if obj.party_admin == 1:
            count = obj.linked_party.count()
            url = (
                reverse("admin:invite_guest_changelist")
                + "?"
                + urlencode({"guest__id": f"{obj.id}"})
            )
            return format_html('<a href="{}">{} Guests</a>', url, count)
        else:
            return format_html('N/A')


@admin.register(Wedding)
class WeddingAdmin(admin.ModelAdmin):
    list_display = ("wedding_date", "to_be_wed1", "to_be_wed2", "active")

    def to_be_wed1(self, obj):
        tbw = obj.couple.all()
        return tbw[0]

    def to_be_wed2(self, obj):
        tbw = obj.couple.all()
        return tbw[1]


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    pass


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ("song", "artist")


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "website")


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("description", "date_added", "order")


@admin.register(Message)
class MessageAdmin(SummernoteModelAdmin):
    summernote_field = ('description')
