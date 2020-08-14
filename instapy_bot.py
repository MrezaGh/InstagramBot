from instapy import InstaPy


class InstaPyBot:
    def __init__(self, username, password):
        self.session = InstaPy(username=username, password=password)
        self.session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)

    def login(self):
        self.session.login()

    def like_by_tag(self, tags, amount=5):
        self.session.like_by_tags(tags, amount)

    def follow(self, percentage):
        self.session.set_do_follow(True, percentage)

    def block_tags(self, tags):
        self.session.set_dont_like(tags)

    def comment(self, percentage, comments=None):
        if not comments:
            comments = ["Nice!", "Sweet!", "Beautiful :heart_eyes:"]
        self.session.set_do_comment(True, percentage)
        self.session.set_comments(comments)
