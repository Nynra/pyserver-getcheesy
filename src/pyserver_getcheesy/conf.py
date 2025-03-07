from django.conf import settings
from appconf import AppConf
from django.utils import timezone


class PyserverGetcheesyAppConf(AppConf):
    ADMIN_GROUP_NAME = "getcheesy_admin"
    GETCHEESY_CREATOR_GROUP_NAME = "getcheesy_creator"
    GETCHEESY_CONSUMER_GROUP_NAME = "getcheesy_consumer"

    class Meta:
        # Make this setting module a proxy for the global settings
        # so we can use this module to access all the settings
        proxy = True
