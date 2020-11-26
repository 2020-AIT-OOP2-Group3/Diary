from diaries.AbstractDiary import AbstractDiary

class MorinagaDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "GitHubDesktopが便利だと知った"

    def get_author(self):
        return "Morinaga"