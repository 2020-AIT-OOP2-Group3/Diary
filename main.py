from diaries.DiarySample import DiarySample
from diaries.KuwabaraDiary import DiaryKuwabara
from diaries.MatsunagaDiaryNew import MatsunagaSample
from diaries.ShimuraDiaryNew import ShimuraDiaryNew
from diaries.ShinoharaDiaryNew import ShinoharaDiaryNew

diaries = [
    DiarySample(),
    ShinoharaDiaryNew(),
    ShimuraDiaryNew(),
    MatsunagaSample(),
    DiaryKuwabara(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
