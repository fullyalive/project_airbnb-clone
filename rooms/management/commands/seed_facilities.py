from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "Facilities를 생성하기 위한 커맨드입니다."

    def handle(self, *args, **options):
        facilities = ["수영장", "자쿠지욕조", "헬스장", "엘리베이터", "건물 내 무료주차"]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities 생성완료!"))
