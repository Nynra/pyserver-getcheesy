from pyserver_tools.utils import create_group
from django.core.management.base import BaseCommand
from pyserver_getcheesy.conf import settings


class Command(BaseCommand):
    help = "Create groups for getcheesy"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            default=False,
            action="store_true",
            help="Force the creation of the groups",
        )
        parser.add_argument(
            "--verbose",
            action="store_true",
            default=True,
            help="Print verbose output to the console",
        )

    def handle(self, *args, **options):
        create_group(
            self,
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            permissions=[
                "change_receiverconfiguration",
                "delete_receiverconfiguration",
                "view_receiverconfiguration",
                "add_compliment",
                "change_compliment",
                "delete_compliment",
                "view_compliment",
                "can_read_random_compliment",
                "add_cheesyjoke",
                "change_cheesyjoke",
                "delete_cheesyjoke",
                "view_cheesyjoke",
                "can_read_random_joke",
                "add_cheesyquote",
                "change_cheesyquote",
                "delete_cheesyquote",
                "view_cheesyquote",
                "can_read_random_quote"
            ],
            force=options["force"],
            verbose=options["verbose"],
            raise_exceptions=False,
        )
        create_group(
            self,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
            permissions=[
                "add_compliment",
                "change_compliment",
                "delete_compliment",
                "view_compliment",
                "can_read_random_compliment",
                "add_cheesyjoke",
                "change_cheesyjoke",
                "delete_cheesyjoke",
                "view_cheesyjoke",
                "can_read_random_joke",
                "add_cheesyquote",
                "change_cheesyquote",
                "delete_cheesyquote",
                "view_cheesyquote",
                "can_read_random_quote"
            ],
            force=options["force"],
            verbose=options["verbose"],
            raise_exceptions=False,
        )
        create_group(
            self,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
            permissions=[
                "view_compliment",
                "can_read_random_compliment",
                "view_cheesyjoke",
                "can_read_random_joke",
                "view_cheesyquote",
                "can_read_random_quote"
            ],
            force=options["force"],
            verbose=options["verbose"],
            raise_exceptions=False,
        )

