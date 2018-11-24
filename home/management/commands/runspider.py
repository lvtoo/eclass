# coding=utf-8
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 启动 教务处新闻
        import home.robot.robot_jwc_news_info
        # 启动 讲座通知
        import home.robot.robot_note_info

    pass
