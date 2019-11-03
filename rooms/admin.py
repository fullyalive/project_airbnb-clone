from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    list_display = ("name", "used_by")

    def used_by(self, obj):
        return obj.rooms.count()

    pass


class PhotoInline(admin.TabularInline):

    model = models.Photo


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    inlines = (PhotoInline,)

    fieldsets = (
        ("호스트정보", {"fields": ("host",)}),
        (
            "기본정보",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("운영정보", {"fields": ("check_in", "check_out", "instant_book")}),
        ("방정보", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "시설정보",
            {
                # "classes": ("collapse",),
                "fields": ("facilities", "amenities", "house_rules")
            },
        ),
    )

    ordering = ("name", "price", "bedrooms")

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
        "count_photos",
        "count_amenities",
        "total_rating",
    )

    list_filter = ("host__superhost", "instant_book", "room_type", "facilities", "city")

    raw_id_fields = ("host",)  # 유저가 많아질 때 foreign key를 통해 host 를 더 나은 방법으로 찾기 위해서

    search_fields = ("^city", "^host__username")

    filter_horizontal = ("facilities", "amenities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    def count_photos(self, obj):
        return obj.photos.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    # pass
    list_display = ("get_thumbnail", "__str__")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "썸네일 이미지"
