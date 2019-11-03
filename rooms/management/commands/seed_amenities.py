from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "Amenities를 생성하기 위한 커맨드입니다."

    def handle(self, *args, **options):
        amenities = [
            "에어컨",
            "알람시계",
            "발코니",
            "화장실",
            "욕조",
            "침대보",
            "보트 시설",
            "케이블 TV",
            "일산화탄소 감지기",
            "의자",
            "어린이 놀이공간",
            "커피메이커",
            "요리판",
            "조리기구 및 주방용품",
            "식기세척기",
            "더블 베드",
            "실내 욕실",
            "무료 주차",
            "무선 인터냇",
            "냉동고",
            "냉장고",
            "골프시설",
            "헤어 드라이기",
            "난방시설",
            "온수 욕조",
            "실내수영장",
            "다림판",
            "전자레인지",
            "야외수영장",
            "테니스 시설",
            "오븐",
            "퀸사이즈 침대",
            "래스토랑",
            "쇼핑몰",
            "샤워시설",
            "화재감지기",
            "소파",
            "음향시설",
            "수영장",
            "타월",
            "TV",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} Amenities 생성완료!"))
