from diaries.DiarySample import DiarySample
from diaries.MatsunagaDiaryNew import MatsunagaSample

diaries = [
    DiarySample(),
    MatsunagaSample(),
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()