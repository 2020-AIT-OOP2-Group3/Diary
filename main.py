from diaries.DiarySample import DiarySample
from diaries.KuwabaraDiary import DiaryKuwabara

diaries = [DiarySample(),DiaryKuwabara() ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()