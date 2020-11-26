from diaries.AbstractDiary import AbstractDiary


class ShinoharaDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "大変な一日だった"

    def get_author(self):
        return "Shinohara"