from diaries.AbstractDiary import AbstractDiary


class YamagutiDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "グループワークが始まった。"

    def get_author(self):
        return "Yamaguti"