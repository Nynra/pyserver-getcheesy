from django.contrib import admin
from pyserver_getcheesy.forms import (
    CheesyJokeChangeForm,
    CheesyJokeCreationForm,
    CheesyQuoteChangeForm,
    CheesyQuoteCreationForm,
    ComplimentChangeForm,
    ComplimentCreationForm,
    ReceiverConfigurationChangeForm,
    ReceiverConfigurationCreationForm,
)
from pyserver_getcheesy.models import (
    CheesyJoke,
    CheesyQuote,
    Compliment,
    ReceiverConfiguration,
)


class CheesyJokeAdmin(admin.ModelAdmin):
    add_form = CheesyJokeCreationForm
    form = CheesyJokeChangeForm
    model = CheesyJoke
    list_display = [
        "id",
        "joke",
        "user_config",
        "repeat",
        "on_specific_date",
        "is_active",
        "last_used",
    ]
    list_filter = [
        "is_active",
        "repeat",
        "on_specific_date",
        "user_config",
        "last_used",
    ]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "joke",
                    "user_config",
                    "repeat",
                    "on_specific_date",
                    "is_active",
                    "last_used",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "joke",
                    "user_config",
                    "repeat",
                    "on_specific_date",
                    "is_active",
                    "last_used",
                ),
            },
        ),
    )
    search_fields = ["joke"]
    ordering = ["joke"]
    filter_horizontal = ()


class CheesyQuoteAdmin(admin.ModelAdmin):
    add_form = CheesyQuoteCreationForm
    form = CheesyQuoteChangeForm
    model = CheesyQuote
    list_display = [
        "id",
        "quote",
        "user_config",
        "repeat",
        "on_specific_date",
        "is_active",
        "last_used",
    ]
    list_filter = ["is_active"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "quote",
                    "user_config",
                    "repeat",
                    "on_specific_date",
                    "is_active",
                    "last_used",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "quote",
                    "user_config",
                    "repeat",
                    "on_specific_date",
                    "is_active",
                    "last_used",
                ),
            },
        ),
    )
    search_fields = ["quote"]
    ordering = ["quote"]
    filter_horizontal = ()


class ComplimentAdmin(admin.ModelAdmin):
    add_form = ComplimentCreationForm
    form = ComplimentChangeForm
    model = Compliment
    list_display = [
        "id",
        "compliment",
        "user_config",
        "repeat",
        "on_specific_date",
        "is_active",
        "last_used",
    ]
    list_filter = ["is_active"]
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "compliment",
                    "user_config",
                    "repeat",
                    "on_specific_date",
                    "is_active",
                    "last_used",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "compliment",
                    "user_config",
                    "repeat",
                    "on_specific_date",
                    "is_active",
                    "last_used",
                ),
            },
        ),
    )
    search_fields = ["compliment"]
    ordering = ["compliment"]
    filter_horizontal = ()


class ReceiverConfigurationAdmin(admin.ModelAdmin):
    add_form = ReceiverConfigurationCreationForm
    form = ReceiverConfigurationChangeForm
    model = ReceiverConfiguration
    list_display = ["id", "user", "receiver"]
    list_filter = ["user"]
    fieldsets = ((None, {"fields": ("user", "receiver")}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("user", "receiver"),
            },
        ),
    )
    search_fields = ["user"]
    ordering = ["user"]
    filter_horizontal = ()


admin.site.register(CheesyJoke, CheesyJokeAdmin)
admin.site.register(CheesyQuote, CheesyQuoteAdmin)
admin.site.register(Compliment, ComplimentAdmin)
admin.site.register(ReceiverConfiguration, ReceiverConfigurationAdmin)
