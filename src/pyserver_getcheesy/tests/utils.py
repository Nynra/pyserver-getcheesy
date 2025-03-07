from users.models import CustomUser as User
from pyserver_getcheesy.models import (
    CheesyJoke,
    CheesyQuote,
    Compliment,
    ReceiverConfiguration,
)
from django.utils import timezone
import datetime


def add_objects(model_class, n: int, sender: User, receiver: User) -> list:
    """Add n objects to the database."""
    # Create a user configuration
    user_config = ReceiverConfiguration.objects.create(
        user=sender,
        receiver=receiver,
    )

    objects = []
    for i in range(n):
        objects.append(
            model_class.objects.create(
                is_active=True,
                user_config=user_config,
                # Activate yesterday
                activation_date=timezone.now() - datetime.timedelta(days=1),
                pub_date=timezone.now(),
                reuse_interval=datetime.timedelta(days=7),
                last_used=timezone.now(),
            )
        )

    return objects
