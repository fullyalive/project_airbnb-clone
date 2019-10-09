from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = ((GENDER_MALE, "남성"), (GENDER_FEMALE, "여성"), (GENDER_OTHER, "기타"))

    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(
        default=GENDER_MALE,
        choices=GENDER_CHOICES,
        max_length=10,
        null=True,
        blank=True,
    )
    bio = models.TextField(default="", blank=True)
