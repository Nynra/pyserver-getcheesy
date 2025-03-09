from django import forms
from django.forms import ModelForm as BaseModelForm
from pyserver_getcheesy.models import (
    CheesyQuote,
    CheesyJoke,
    Compliment,
    ReceiverConfiguration,
)
from django.contrib.auth import get_user_model
from django.db.models import Q
from django.utils import timezone


User = get_user_model()


class BaseCreationForm(BaseModelForm):
    """Base creation form for randomizable models"""

    user_config = forms.ModelChoiceField(
        queryset=ReceiverConfiguration.objects.all(),
    )
    is_active = forms.BooleanField(
        required=False,
    )
    activation_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        initial=timezone.now(),
    )
    repeat = forms.BooleanField(
        required=False,
    )
    repeat_interval = forms.TimeInput(
        attrs={"type": "time"},
    )
    on_specific_date = forms.BooleanField(
        required=False,
    )
    specific_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
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


class BaseChangeForm(BaseCreationForm):
    pass


class BaseDetailForm(BaseModelForm):
    user_config = forms.ModelChoiceField(
        queryset=ReceiverConfiguration.objects.all(),
        widget=forms.TextInput(attrs={"readonly": True}),
    )
    is_active = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"readonly": True}),
    )
    activation_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"readonly": True}),
    )
    repeat = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"readonly": True}),
    )
    repeat_interval = forms.TimeInput(
        attrs={"readonly": True},
    )
    on_specific_date = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"readonly": True}),
    )
    specific_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"readonly": True}),
    )
    last_used = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={"readonly": True}),
    )

    def __init__(self, *args, **kwargs):
        # try:
        #     user = kwargs.pop("request_user")
        # except KeyError:
        #     raise ValueError("request_user must be passed as a keyword argument")
        
        super().__init__(*args, **kwargs)



class BaseDeleteForm(BaseDetailForm):
    
    def __init__(self, *args, **kwargs):
        self.request_user = kwargs.pop("request_user")
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        if self.instance.user != self.request_user:
            raise forms.ValidationError("User is not the owner of the object")
        return cleaned_data


class CheesyQuoteCreationForm(BaseCreationForm):
    quote = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 40}),
    )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
        ]


class CheesyQuoteDeleteForm(BaseDeleteForm):
    quote = forms.CharField(
        widget=forms.Textarea(attrs={"readonly": True, "rows": 3, "cols": 40}),
    )
    
    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class CheesyQuoteRandomForm(BaseModelForm):
    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
        ]


class CheesyQuoteDetailForm(BaseDetailForm):
    quote = forms.CharField(
        widget=forms.Textarea(attrs={"readonly": True, "rows": 3, "cols": 40}),
    )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class CheesyQuoteChangeForm(BaseChangeForm):
    quote = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 40}),
    )

    class Meta:
        model = CheesyQuote
        fields = [
            "quote",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
        ]


class CheesyJokeCreationForm(BaseCreationForm):
    joke = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 40}),
    )

    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
        ]


class CheesyJokeDeleteForm(BaseDeleteForm):
    joke = forms.CharField(
        widget=forms.Textarea(attrs={"readonly": True, "rows": 3, "cols": 40}),
    )
    
    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class CheesyJokeRandomForm(BaseModelForm):
    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
        ]


class CheesyJokeDetailForm(BaseDetailForm):
    joke = forms.CharField(
        widget=forms.Textarea(attrs={"readonly": True, "rows": 3, "cols": 40}),
    )

    class Meta:
        model = CheesyJoke
        fields = [
            "joke",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class CheesyJokeChangeForm(BaseModelForm):

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
            "repeat_interval",
            "on_specific_date",
            "specific_date",
        ]


class ComplimentCreationForm(BaseCreationForm):
    compliment = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 40}),
    )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
        ]


class ComplimentDeleteForm(BaseDeleteForm):
    compliment = forms.CharField(
        widget=forms.Textarea(attrs={"readonly": True, "rows": 3, "cols": 40}),
    )
    
    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class ComplimentRandomForm(BaseModelForm):
    class Meta:
        model = Compliment
        fields = [
            "compliment",
        ]


class ComplimentDetailForm(BaseDetailForm):
    compliment = forms.CharField(
        widget=forms.Textarea(attrs={"readonly": True, "rows": 3, "cols": 40}),
    )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
            "last_used",
        ]


class ComplimentChangeForm(BaseChangeForm):
    compliment = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 3, "cols": 40}),
    )

    class Meta:
        model = Compliment
        fields = [
            "compliment",
            "user_config",
            "is_active",
            "activation_date",
            "repeat",
            "repeat_interval",
            "on_specific_date",
            "specific_date",
        ]


class ReceiverConfigurationCreationForm(BaseModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("request_user")
        super().__init__(*args, **kwargs)
        self.fields["receiver"].queryset = User.objects.filter(~Q(id=user.id))

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
        queryset=User.objects.all(), widget=forms.TextInput(attrs={"readonly": True})
    )

    class Meta:
        model = ReceiverConfiguration
        fields = ["receiver"]


class ReceiverConfigurationChangeForm(BaseModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all())

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
