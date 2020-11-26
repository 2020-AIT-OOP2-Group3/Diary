from diaries.AbstractDiary import AbstractDiary


class ShimuraDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "講義の話を聞きながら日記を書いた。"

    def get_author(self):
        return "Shimura"
