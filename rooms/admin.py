from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    fieldsets = (
        ("호스트정보", {"fields": ("host",)}),
        ("기본정보", {"fields": ("name", "description", "country", "address", "price")}),
        ("운영정보", {"fields": ("check_in", "check_out", "instant_book")}),
        ("방정보", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "시설정보",
            {
                "classes": ("collapse",),
                "fields": ("facilities", "amenities", "house_rules"),
            },
        ),
    )

    ordering = ('name', 'price', 'bedrooms')

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    list_filter = ("host__superhost", "instant_book", "room_type", "facilities", "city")

    search_fields = ("^city", "^host__username")

    filter_horizontal = ("facilities", "amenities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
