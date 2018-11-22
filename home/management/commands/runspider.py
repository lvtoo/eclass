# coding=utf-8
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        import home.robot.robot_jwc_info
        import home.robot.robot_note_info
    pass
