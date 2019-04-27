# coding=utf-8
from django.core.management.base import BaseCommand
import sys


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 启动 教务处新闻
        import home.robot.robot_jwc_news_info
        # 启动 讲座通知
        import home.robot.robot_note_info
        # 启动 校园动态
        import home.robot.robot_campus_news_info
        # 启动 教务处新闻
        # import home.robot.robot_jwc_notes_info

    pass
