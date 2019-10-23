from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "in_progress",
        "room",
        "status",
        "guest",
        "check_in",
        "check_out",
    )

    list_filter = ("status",)
