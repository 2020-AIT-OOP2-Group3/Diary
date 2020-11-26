from diaries.DiarySample import DiarySample
from diaries.ShinoharaDiaryNew import ShinoharaDiaryNew

diaries = [DiarySample(), ShinoharaDiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()