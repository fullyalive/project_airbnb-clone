from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "django_seed를 이용해 User를 생성하기 위한 커맨드입니다."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="얼마나 많은 유저를 생성하기 원하십니까?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}명 유저 생성완료!"))
