from diaries.DiarySample import DiarySample
from diaries.ShimuraDiaryNew import ShimuraDiaryNew
from diaries.ShinoharaDiaryNew import ShinoharaDiaryNew

diaries = [DiarySample(), ShinoharaDiaryNew(), ShimuraDiaryNew()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
