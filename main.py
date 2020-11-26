from diaries.DiarySample import DiarySample
from diaries.KuwabaraDiary import DiaryKuwabara
from diaries.MatsunagaDiaryNew import MatsunagaSample
from diaries.ShimuraDiaryNew import ShimuraDiaryNew
from diaries.ShinoharaDiaryNew import ShinoharaDiaryNew
from diaries.YamagutiDiaryNew import YamagutiDiaryNew

diaries = [
    DiarySample(),
    ShinoharaDiaryNew(),
    ShimuraDiaryNew(),
    MatsunagaSample(),
    DiaryKuwabara(),
    YamagutiDiaryNew(), 
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
