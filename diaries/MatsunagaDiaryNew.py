from diaries.AbstractDiary import AbstractDiary


class MatsunagaSample(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "よろしくお願いします。"

    def get_author(self):
        return "Matsunaga"