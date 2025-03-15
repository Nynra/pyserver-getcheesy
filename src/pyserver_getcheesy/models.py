from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.exceptions import ValidationError
from collections.abc import Collection
import random
import datetime


class ReceiverConfiguration(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="user"
    )
    receiver = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="receiver"
    )

    def clean_fields(self, exclude: Collection[str] | None = ...) -> None:
        if self.user == self.receiver:
            raise ValidationError("User and receiver cannot be the same")

        # Check if this user already has a config with this receiver
        if ReceiverConfiguration.objects.filter(
            user=self.user, receiver=self.receiver
        ).exists():
            raise ValidationError("This user already has a config with this receiver")

        return super().clean_fields(exclude)

    def __str__(self):
        return self.user.username + " - " + self.receiver.username


class BaseRamdomizableModel(models.Model):
    # Some tracking info
    id = models.AutoField(primary_key=True, auto_created=True)
    is_active = models.BooleanField(default=True)
    # Set the activation date to yesterday
    activation_date = models.DateTimeField(
        "activation date",
        default=timezone.now,
        null=False,
        blank=False,
    )
    pub_date = models.DateTimeField("date published", default=timezone.now)

    # Only repeat the message if repeat is True
    repeat = models.BooleanField(default=True)
    repeat_interval_weeks = models.IntegerField(default=1, blank=True, null=True)
    repeat_interval_days = models.IntegerField(default=0, blank=True, null=True)
    repeat_interval_hours = models.IntegerField(default=0, blank=True, null=True)
    repeat_interval_minutes = models.IntegerField(default=0, blank=True, null=True)

    # If on_specific_day is True, the message will only be sent on the specific_day
    # each year. This can be combined with repeat
    on_specific_date = models.BooleanField(default=False)
    specific_date = models.DateField(
        "specific date", default=timezone.now, null=True, blank=True
    )

    # last used field should be updated when the message is used
    last_used = models.DateTimeField("last used", default=timezone.now)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        # Check if we have an id, if not, we are creating a new object
        if not self.id:
            self.pub_date = timezone.now()
        self.last_used = timezone.now()
        return super().save(*args, **kwargs)

    def update_activation_date(self):
        self.last_used = timezone.now()

        # Set the repeat interval or disable the message
        if self.repeat:
            self.activation_date = timezone.now() + self.get_repeat_interval()
        else:
            self.is_active = False
        self.save()

    def get_repeat_interval(self) -> datetime.timedelta:
        """Return the repeat interval as a timedelta."""
        return datetime.timedelta(
            weeks=self.repeat_interval_weeks,
            days=self.repeat_interval_days,
            hours=self.repeat_interval_hours,
            minutes=self.repeat_interval_minutes,
        )

    @staticmethod
    def _get_random_index(max_index) -> int:
        """Return a random index."""
        random_index = random.randint(0, max_index - 1)
        random_index %= max_index
        return random_index

    @classmethod
    def get_random(cls, user):
        """Only return objects that have not been used sinds now - interval time."""
        # Get the user configurations where the user is the receiver
        user_configurations = ReceiverConfiguration.objects.filter(receiver=user.id)

        # Get the active messages with this config and an activation date in the past
        active_messages = cls.objects.filter(
            user_config__in=user_configurations,
            activation_date__lte=timezone.now(),
            is_active=True,
        )

        # For the messages with on_specific_date, check if the specific date is today
        active_messages = [
            message
            for message in active_messages
            if not message.on_specific_date
            or (
                message.on_specific_date
                and message.specific_date == timezone.now().date()
            )
        ]

        # Get the random index
        # if there are no active messages, return None
        # else return the random message
        if len(active_messages) == 0:
            return None
        else:
            random_index = cls._get_random_index(len(active_messages))
            message = active_messages[random_index]
            message.update_activation_date()
            return message


class CheesyQuote(BaseRamdomizableModel):
    user_config = models.ForeignKey(
        ReceiverConfiguration,
        on_delete=models.CASCADE,
        related_name="quote_user_config",
    )
    quote = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_read_random_quote", "Can read a random quote"),
        ]

    def __str__(self):
        return self.quote


class CheesyJoke(BaseRamdomizableModel):
    user_config = models.ForeignKey(
        ReceiverConfiguration, on_delete=models.CASCADE, related_name="joke_user_config"
    )
    joke = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_read_random_joke", "Can read a random joke"),
        ]
        pass

    def __str__(self):
        return self.joke


class Compliment(BaseRamdomizableModel):
    user_config = models.ForeignKey(
        ReceiverConfiguration,
        on_delete=models.CASCADE,
        related_name="compliment_user_config",
    )
    compliment = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_read_random_compliment", "Can read a random compliment"),
        ]
        pass

    def __str__(self):
        return self.compliment
