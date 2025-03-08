from django import forms
from pyserver_getcheesy.models import (
    CheesyQuote,
    CheesyJoke,
    Compliment,
    ReceiverConfiguration,
)


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CheesyQuoteCreationForm(BaseModelForm):

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

    # Only allow user configs of wich the user is the creator
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
            user=user
        )

    # Can this also be done in the form?
    # def clean_user_config(self):
    #     user_config = self.cleaned_data["user_config"]
    #     if user_config.receiver != self.request.user:
    #         raise forms.ValidationError("You can only create quotes for yourself")
    #     return user_config

    # We need to make sure the user only sees the user configs that belong to them
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user")
    #     super().__init__(*args, **kwargs)
    #     self.fields["user_config"].queryset = ReceiverConfiguration.objects.filter(
    #         receiver=user
    #     )


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


# class FactCreationForm(BaseModelForm):
#     class Meta:
#         model = Fact
#         fields = [
#             "fact",
#             "activation_date",
#             "user_config",
#             "repeat",
#             "repeat_interval",
#             "on_specific_date",
#             "specific_date",
#             "is_active",
#         ]


# class FactRandomForm(BaseModelForm):
#     class Meta:
#         model = Fact
#         fields = [
#             "fact",
#         ]


# class FactDetailForm(BaseModelForm):
#     class Meta:
#         model = Fact
#         fields = [
#             "fact",
#             "activation_date",
#             "user_config",
#             "repeat",
#             "repeat_interval",
#             "on_specific_date",
#             "specific_date",
#             "last_used",
#             "is_active",
#         ]

#         # Make all fields read only
#         widgets = {
#             "fact": forms.TextInput(attrs={"readonly": True}),
#             "activation_date": forms.TextInput(attrs={"readonly": True}),
#             "user_config": forms.TextInput(attrs={"readonly": True}),
#             "repeat": forms.TextInput(attrs={"readonly": True}),
#             "repeat_interval": forms.TextInput(attrs={"readonly": True}),
#             "on_specific_date": forms.TextInput(attrs={"readonly": True}),
#             "specific_date": forms.TextInput(attrs={"readonly": True}),
#             "last_used": forms.TextInput(attrs={"readonly": True}),
#             "is_active": forms.TextInput(attrs={"readonly": True}),
#         }


# class FactChangeForm(BaseModelForm):
#     class Meta:
#         model = Fact
#         fields = [
#             "fact",
#             "activation_date",
#             "user_config",
#             "reuse_interval",
#             "active_window_start_date",
#             "active_window_start_time",
#             "active_window_duration",
#             "is_active",
#         ]


class ReceiverConfigurationCreationForm(BaseModelForm):
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
    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]
