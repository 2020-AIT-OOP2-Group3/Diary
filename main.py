from diaries.DiarySample import DiarySample
from diaries.MatsunagaDiaryNew import MatsunagaSample
from diaries.ShinoharaDiaryNew import ShinoharaDiaryNew

diaries = [
    DiarySample(),
    MatsunagaSample(),
    ShinoharaDiaryNew(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()