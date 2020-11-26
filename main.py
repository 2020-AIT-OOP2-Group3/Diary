from diaries.DiarySample import DiarySample
from diaries.ShinoharaDiaryNew import ShinoharaDiaryNew
from diaries.YamagutiDiaryNew import YamagutiDiaryNew

diaries = [
    DiarySample(), 
    ShinoharaDiaryNew(), 
    YamagutiDiaryNew(), 
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()