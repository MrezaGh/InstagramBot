from instapy import InstaPy


class InstaPyBot:
    def __init__(self, username, password):
        self.session = InstaPy(username=username, password=password)
        self.session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

    def login(self):
        self.session.login()
