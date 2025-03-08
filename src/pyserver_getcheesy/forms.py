from django import forms
from pyserver_getcheesy.models import (
    CheesyQuote,
    CheesyJoke,
    Compliment,
    ReceiverConfiguration,
)
from django.contrib.auth import get_user_model
from django.db.models import Q


User = get_user_model()


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CheesyQuoteCreationForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "is_active",
        ]


class CheesyQuoteRandomForm(BaseModelForm):
    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
        ]


class CheesyQuoteDetailForm(BaseModelForm):
    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
            "is_active",
        ]

        # Make all the fields read only
        widgets = {
            "quote": forms.TextInput(attrs={"readonly": True}),
            "activation_date": forms.TextInput(attrs={"readonly": True}),
            "user_config": forms.TextInput(attrs={"readonly": True}),
            "repeat": forms.TextInput(attrs={"readonly": True}),
            "repeat_interval": forms.TextInput(attrs={"readonly": True}),
            "on_specific_date": forms.TextInput(attrs={"readonly": True}),
            "specific_date": forms.TextInput(attrs={"readonly": True}),
            "last_used": forms.TextInput(attrs={"readonly": True}),
            "is_active": forms.TextInput(attrs={"readonly": True}),
        }


class CheesyQuoteChangeForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "is_active",
        ]


class CheesyJokeCreationForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "is_active",
        ]


class CheesyJokeRandomForm(BaseModelForm):
    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
        ]


class CheesyJokeDetailForm(BaseModelForm):
    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
            "is_active",
        ]

        # Make all fields read only
        widgets = {
            "joke": forms.TextInput(attrs={"readonly": True}),
            "activation_date": forms.TextInput(attrs={"readonly": True}),
            "user_config": forms.TextInput(attrs={"readonly": True}),
            "repeat": forms.TextInput(attrs={"readonly": True}),
            "repeat_interval": forms.TextInput(attrs={"readonly": True}),
            "on_specific_date": forms.TextInput(attrs={"readonly": True}),
            "specific_date": forms.TextInput(attrs={"readonly": True}),
            "last_used": forms.TextInput(attrs={"readonly": True}),
            "is_active": forms.TextInput(attrs={"readonly": True}),
        }


class CheesyJokeChangeForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "is_active",
        ]


class ComplimentCreationForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "is_active",
        ]


class ComplimentRandomForm(BaseModelForm):
    class Meta:
        model = Compliment
        fields = [
            "compliment",
        ]


class ComplimentDetailForm(BaseModelForm):
    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
            "is_active",
        ]

        # Make all fields read only
        widgets = {
            "compliment": forms.TextInput(attrs={"readonly": True}),
            "activation_date": forms.TextInput(attrs={"readonly": True}),
            "user_config": forms.TextInput(attrs={"readonly": True}),
            "repeat": forms.TextInput(attrs={"readonly": True}),
            "repeat_interval": forms.TextInput(attrs={"readonly": True}),
            "on_specific_date": forms.TextInput(attrs={"readonly": True}),
            "specific_date": forms.TextInput(attrs={"readonly": True}),
            "last_used": forms.TextInput(attrs={"readonly": True}),
            "is_active": forms.TextInput(attrs={"readonly": True}),
        }


class ComplimentChangeForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "activation_date",
            "user_config",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "is_active",
        ]


class ReceiverConfigurationCreationForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["receiver"].queryset = User.objects.filter(
            ~Q(id=user.id)
        )

    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]


class ReceiverConfigurationDetailForm(BaseModelForm):
    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]

        # Make all fields read only
        widgets = {
            "receiver": forms.TextInput(attrs={"readonly": True}),
        }


class ReceiverConfigurationChangeForm(BaseModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        # The receiver cannot be the same as the user
        # and cannot be in nother receiver configuration of the user
        self.fields["receiver"].queryset = User.objects.filter(
            ~Q(id=user.id)
        ).exclude(
            id__in=ReceiverConfiguration.objects.filter(user=user).values("receiver")
        )

    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]
