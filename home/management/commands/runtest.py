# coding=utf-8
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        import home.views
        home.views.index(request='')
        pass
