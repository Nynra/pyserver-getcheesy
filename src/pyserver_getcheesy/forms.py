from django import forms
from django.forms import ModelForm as BaseModelForm
from pyserver_getcheesy.models import (
    CheesyQuote,
    CheesyJoke,
    Compliment,
    ReceiverConfiguration,
)
from django.contrib.auth import get_user_model
from pyserver_getcheesy.conf import settings
from django.db.models import Q
from django.utils import timezone


User = get_user_model()


class BaseCreationForm(BaseModelForm):
    """Base creation form for randomizable models"""

    user_config = forms.ModelChoiceField(
        queryset=ReceiverConfiguration.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    is_active = forms.BooleanField(
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    activation_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        ),
        initial=timezone.now(),
    )
    repeat = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
    repeat_interval_weeks = forms.IntegerField(
        label="Weeks",
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": 0}),
    )
    repeat_interval_days = forms.IntegerField(
        label="Days",
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": 0}),
    )
    repeat_interval_hours = forms.IntegerField(
        label="Hours",
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": 0}),
    )
    repeat_interval_minutes = forms.IntegerField(
        label="Minutes",
        required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": 0}),
    )
    on_specific_date = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input", "type": "checkbox"}),
    )
    specific_date = forms.DateTimeField(
        label="",
        widget=forms.DateTimeInput(
            attrs={"type": "datetime-local", "class": "form-control"}
        ),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        try:
            user = kwargs.pop("request_user")
        except KeyError:
            raise ValueError("request_user must be passed as a keyword argument")

        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    # def clean(self):
    #     """Combine fields into a single timezone.timedelta object"""
    #     cleaned_data = super().clean()

    #     days = cleaned_data.get("duration_days") or 0
    #     hours = cleaned_data.get("duration_hours") or 0
    #     minutes = cleaned_data.get("duration_minutes") or 0
    #     seconds = cleaned_data.get("duration_seconds") or 0

    #     # Convert to timedelta
    #     cleaned_data["repeat_interval"] = timezone.timedelta(
    #         days=days, hours=hours, minutes=minutes, seconds=seconds
    #     )
    #     return cleaned_data


class BaseChangeForm(BaseCreationForm):
    pass


class BaseDetailForm(BaseModelForm):
    user_config = forms.ModelChoiceField(
        queryset=ReceiverConfiguration.objects.all(),
        widget=forms.TextInput(attrs={"readonly": True, "class": "form-control"}),
    )
    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"readonly": True, "class": "form-check-input"}
        ),
    )
    activation_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"readonly": True, "class": "form-control"}),
    )
    repeat = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"readonly": True, "class": "form-check-input"}
        ),
    )
    repeat_interval_weeks = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "readonly": True, 
            "class": "form-control",
            "placeholder": 0,
            }
        ),
    )
    # Set the repeat interval to 0 if it is None
    repeat_interval_days = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            "readonly": True, 
            "class": "form-control",
            "placeholder": 0,
            }
        ),
    )
    repeat_interval_hours = forms.IntegerField(
        widget=forms.NumberInput(attrs={"readonly": True, "class": "form-control"}),
    )
    repeat_interval_minutes = forms.IntegerField(
        widget=forms.NumberInput(attrs={"readonly": True, "class": "form-control"}),
    )
    on_specific_date = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={"readonly": True, "class": "form-check-input"}
        ),
    )
    specific_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"readonly": True, "class": "form-control"}),
    )
    last_used = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"readonly": True, "class": "form-control"}),
    )


class CheesyQuoteCreationForm(BaseCreationForm):
    quote = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter a quote...",
            }
        ),
    )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
        ]


class CheesyQuoteRandomForm(BaseModelForm):

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
        ]


class CheesyQuoteDetailForm(BaseDetailForm):
    quote = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "readonly": True,
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
            }
        ),
    )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class CheesyQuoteChangeForm(BaseChangeForm):
    quote = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter a quote...",
            }
        ),
    )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
        ]


class CheesyJokeCreationForm(BaseCreationForm):
    joke = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter a joke...",
            }
        ),
    )

    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
        ]


class CheesyJokeRandomForm(BaseModelForm):
    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
        ]


class CheesyJokeDetailForm(BaseDetailForm):
    joke = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "readonly": True,
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
            }
        ),
    )

    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class CheesyJokeChangeForm(BaseModelForm):
    joke = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter a joke...",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("request_user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
        ]


class ComplimentCreationForm(BaseCreationForm):
    compliment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter a compliment...",
            }
        ),
    )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
        ]


class ComplimentRandomForm(BaseModelForm):
    class Meta:
        model = Compliment
        fields = [
            "compliment",
        ]


class ComplimentDetailForm(BaseDetailForm):
    compliment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "readonly": True,
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
                "placeholder": "Disabled input here...",
            }
        ),
    )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class ComplimentChangeForm(BaseChangeForm):
    compliment = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "rows": 3,
                "cols": 40,
                "class": "form-control",
                "type": "text",
                "placeholder": "Enter a compliment...",
            }
        ),
    )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval_weeks",
            "repeat_interval_days",
            "repeat_interval_hours",
            "repeat_interval_minutes",
            "on_specific_date",
            "specific_date",
        ]


class ReceiverConfigurationCreationForm(BaseModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Receiver",
        widget=forms.Select(
            attrs={"class": "form-select", "placeholder": "Select a user"}
        ),
    )

    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]


class ReceiverConfigurationDeleteForm(BaseModelForm):
    model_class = ReceiverConfiguration

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("request_user")

        # Check if the user is the owner of the receiver configuration
        if self.instance.user != user:
            raise ValueError("User is not the owner of the receiver configuration")

        super().__init__(*args, **kwargs)


class ReceiverConfigurationDetailForm(BaseModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.TextInput(attrs={"readonly": True, "class": "form-control"}),
    )

    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]


class ReceiverConfigurationChangeForm(BaseModelForm):
    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(), widget=forms.Select(attrs={"class": "form-select"})
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("request_user")
        super().__init__(*args, **kwargs)

        # The receiver cannot be the same as the user
        # and cannot be in nother receiver configuration of the user
        self.fields["receiver"].queryset = User.objects.filter(~Q(id=user.id)).exclude(
            id__in=ReceiverConfiguration.objects.filter(user=user)
        )

    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]
