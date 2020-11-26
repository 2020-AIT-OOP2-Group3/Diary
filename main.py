from diaries.DiarySample import DiarySample
from diaries.MatsunagaDiaryNew import MatsunagaSample
from diaries.ShimuraDiaryNew import ShimuraDiaryNew
from diaries.ShinoharaDiaryNew import ShinoharaDiaryNew

diaries = [
  DiarySample(),
  ShinoharaDiaryNew(),
  ShimuraDiaryNew(),
  MatsunagaSample().
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
