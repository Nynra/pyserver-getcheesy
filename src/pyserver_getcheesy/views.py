from django.db.models.query import QuerySet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import DeleteView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
import logging
from typing import Any
from pyserver_tools.base_views import (
    BaseCreateView,
    BaseUpdateView,
    BaseDetailView,
    BaseListView,
    BaseRandomView,
    BaseDeleteView,
)
from pyserver_getcheesy.models import (
    CheesyQuote,
    CheesyJoke,
    Compliment,
    ReceiverConfiguration,
)
from pyserver_getcheesy.forms import (
    CheesyQuoteDetailForm,
    ReceiverConfigurationDetailForm,
    ComplimentRandomForm,
    CheesyJokeRandomForm,
    CheesyQuoteRandomForm,
    ReceiverConfigurationCreationForm,
    # FactChangeForm,
    # FactCreationForm,
    CheesyJokeDetailForm,
    ComplimentDetailForm,
)

logger = logging.getLogger(__name__)
from pyserver_tools.mixins import HasGroupPermissionMixin
from pyserver_getcheesy.conf import settings


# Create a create, update, delete and list view for each model
# Create a list all view that lists all the models
class ListsAllView(LoginRequiredMixin, HasGroupPermissionMixin, View):

    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ]
    }

    def get_objects(self) -> tuple:
        return (
            CheesyQuote.objects.filter(user_config__user=self.request.user).order_by(
                "-id"
            ),
            CheesyJoke.objects.filter(user_config__user=self.request.user).order_by(
                "-id"
            ),
            Compliment.objects.filter(user_config__user=self.request.user).order_by(
                "-id"
            ),
            ReceiverConfiguration.objects.filter(user=self.request.user).order_by(
                "-receiver"
            ),
        )

    def get(self, request, *args, **kwargs):
        context_data = self._get_pages()
        return render(request, "list_all.html", context=context_data)

    def _get_pages(self):
        # Create a paginators for each model and show the first 10
        quotes, jokes, compliments, configs = self.get_objects()

        quote_paginator = Paginator(quotes, 10)
        joke_paginator = Paginator(jokes, 10)
        compliment_paginator = Paginator(compliments, 10)
        # fact_paginator = Paginator(facts, 10)
        config_paginator = Paginator(configs, 10)

        quote_page_obj = quote_paginator.get_page(1)
        joke_page_obj = joke_paginator.get_page(1)
        compliment_page_obj = compliment_paginator.get_page(1)
        # fact_page_obj = fact_paginator.get_page(1)
        config_page_obj = config_paginator.get_page(1)

        return {
            "quotes": quote_page_obj,
            "jokes": joke_page_obj,
            "compliments": compliment_page_obj,
            # "facts": fact_page_obj,
            "configs": config_page_obj,
        }


class HomeView(LoginRequiredMixin, HasGroupPermissionMixin, View):
    """The home page for a logged in user."""

    template_name = "home.html"
    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
        ]
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class ChooseRandomView(LoginRequiredMixin, HasGroupPermissionMixin, View):
    """The page where the user can choose a random model from the catagories."""

    template_name = "choose_random.html"
    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
        ]
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CheesyQuoteBaseView(LoginRequiredMixin, HasGroupPermissionMixin):
    model = CheesyQuote
    model_name = "Quote"
    create_view_name = "create-quote"
    update_view_name = "update-quote"
    delete_view_name = "delete-quote"
    detail_view_name = "detail-quote"
    list_view_name = "list-quotes"
    random_view_name = "random-quote"

    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
        ],
        "post": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "put": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "delete": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
    }


class CheesyJokeBaseView(LoginRequiredMixin, HasGroupPermissionMixin):
    model = CheesyJoke
    model_name = "Joke"
    create_view_name = "create-joke"
    update_view_name = "update-joke"
    delete_view_name = "delete-joke"
    detail_view_name = "detail-joke"
    list_view_name = "list-jokes"
    random_view_name = "random-joke"

    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
        ],
        "post": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "put": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "delete": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
    }


class ComplimentBaseView(LoginRequiredMixin, HasGroupPermissionMixin):
    model = Compliment
    model_name = "Compliment"
    create_view_name = "create-compliment"
    update_view_name = "update-compliment"
    delete_view_name = "delete-compliment"
    detail_view_name = "detail-compliment"
    list_view_name = "list-compliments"
    random_view_name = "random-compliment"

    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
        ],
        "post": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "put": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "delete": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
    }


class ReceiverConfigBaseView(LoginRequiredMixin, HasGroupPermissionMixin):
    model = ReceiverConfiguration
    model_name = "Receiver Configuration"
    create_view_name = "create-receiver-config"
    update_view_name = "update-receiver-config"
    delete_view_name = "delete-receiver-config"
    detail_view_name = "detail-receiver-config"
    list_view_name = "list-receiver-configs"

    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
        ],
        "post": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "put": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
        "delete": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ],
    }


# Logout redirect view
class LogoutRedirectView(LoginRequiredMixin, View):
    def get(self, request):
        return redirect("redirect-home")


# Create views
class CheesyQuoteCreateView(
    CheesyQuoteBaseView,
    BaseCreateView,
):
    # template_name = "quote/create_quote.html"
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


class CheesyJokeCreateView(CheesyJokeBaseView, BaseCreateView):
    # template_name = "joke/create_joke.html"
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


class ComplimentCreateView(ComplimentBaseView, BaseCreateView):
    # template_name = "compliment/create_compliment.html"
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


class ReceiverConfigurationCreateView(ReceiverConfigBaseView, View):
    template_name = "create_model.html"
    fields = ["receiver"]

    def form_valid(self, form):
        form.instance.user = self.request.user.id
        valid = super().form_valid(form)
        if not valid:
            logger.warning(
                f"User {self.request.user} tried to create a receiver config with an invalid form."
            )

    def get_context_data(self, **kwargs):
        context = {
            "model_name": self.model_name,
            "list_url": self.list_view_name,
        }
        return context

    def get(self, request):
        form = ReceiverConfigurationCreationForm()
        # Remove the request user and root from the queryset
        form.fields["receiver"].queryset = form.fields["receiver"].queryset.exclude(
            id=request.user.id
        )
        form.fields["receiver"].queryset = form.fields["receiver"].queryset.exclude(
            username="root"
        )
        # Also exclude the users that already have a receiver config
        form.fields["receiver"].queryset = form.fields["receiver"].queryset.exclude(
            receiver__user=request.user
        )
        context_data = self.get_context_data()
        context_data["form"] = form
        return render(request, self.template_name, context=context_data)

    def post(self, request):
        form = ReceiverConfigurationCreationForm(request.POST)
        # Add the user to the form
        form.instance.user = request.user

        if form.is_valid():
            form.save()
            return redirect("list-receiver-configs")
        else:
            # Give the user the errors
            logger.warning(
                f"User {request.user} tried to create a receiver config with an invalid form."
            )
            return render(
                request,
                "error.html",
                context={
                    "errors": form.errors,
                    "previous_page_url": reverse("create-receiver-config"),
                },
            )


# Update views
class CheesyQuoteUpdateView(CheesyQuoteBaseView, BaseUpdateView):
    # template_name = "quote/update_quote.html"
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


class CheesyJokeUpdateView(CheesyJokeBaseView, BaseUpdateView):
    # template_name = "joke/update_joke.html"
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


class ComplimentUpdateView(ComplimentBaseView, BaseUpdateView):
    # template_name = "compliment/update_compliment.html"
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


class ReceiverConfigurationUpdateView(ReceiverConfigBaseView, BaseUpdateView):
    # template_name = "config/update_config.html"
    fields = ["receiver"]


# Delete views
class CheesyQuoteDeleteView(CheesyQuoteBaseView, BaseDeleteView):
    # template_name = "quote/delete_quote.html"
    success_url = "list-quotes"


class CheesyJokeDeleteView(CheesyJokeBaseView, BaseDeleteView):
    # template_name = "joke/delete_joke.html"
    success_url = "list-jokes"


class ComplimentDeleteView(ComplimentBaseView, BaseDeleteView):
    # template_name = "compliment/delete_compliment.html"
    success_url = "list-compliments"


class ReceiverConfigurationDeleteView(ReceiverConfigBaseView, DeleteView):
    success_url = "list-receiver-config"
    template_name = "delete_model.html"
    context_object_name = "item"

    def form_valid(self, form):
        # Check if the user field matches the request user
        if self.object.user != self.request.user:
            logger.error(
                f"User {self.request.user} tried to delete a receiver config that does not belong to them."
            )
            return self.form_invalid(form)
        valid = super().form_valid(form)
        if not valid:
            logger.warning(
                f"User {self.request.user} tried to delete a receiver config with an invalid form."
            )

    def get_success_url(self) -> str:
        logger.info(
            "User {} deleted a {}, with id {}".format(
                self.request.user, self.model.__name__, self.object.pk
            )
        )
        return reverse_lazy(self.list_view_name)

    # For the template to render correctly the model name variable and list url have to be passed
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["model_name"] = self.model_name
        context["list_url"] = self.list_view_name
        return context


# Detail views
class CheesyQuoteDetailView(CheesyQuoteBaseView, BaseDetailView):
    # template_name = "quote/detail_quote.html"
    detail_form = CheesyQuoteDetailForm


class CheesyJokeDetailView(CheesyJokeBaseView, BaseDetailView):
    # template_name = "joke/detail_joke.html"
    detail_form = CheesyJokeDetailForm


class ComplimentDetailView(ComplimentBaseView, BaseDetailView):
    # template_name = "compliment/detail_compliment.html"
    detail_form = ComplimentDetailForm


# class FactDetailView(FactBaseView, GetCheesyFactPermissionMixin, BaseDetailView):
#     detail_form = FactChangeForm


class ReceiverConfigurationDetailView(ReceiverConfigBaseView, BaseDetailView):
    # template_name = "config/detail_config.html"
    detail_form = ReceiverConfigurationDetailForm


# Random views
class RandomQuoteView(CheesyQuoteBaseView, BaseRandomView):
    # template_name = "quote/random_quote.html"
    form_class = CheesyQuoteRandomForm

class RandomJokeView(CheesyJokeBaseView, BaseRandomView):
    # template_name = "joke/random_joke.html"
    form_class = CheesyJokeRandomForm


class RandomComplimentView(ComplimentBaseView, BaseRandomView):
    # template_name = "compliment/random_compliment.html"
    form_class = ComplimentRandomForm


# List views
class CheesyQuoteListView(CheesyQuoteBaseView, BaseListView):
    # template_name = "quote/list_quotes.html"
    pass


class CheesyJokeListView(CheesyJokeBaseView, BaseListView):
    # template_name = "joke/list_jokes.html"
    pass


class ComplimentListView(ComplimentBaseView, BaseListView):
    # template_name = "compliment/list_compliments.html"
    pass


class ReceiverConfigurationListView(ReceiverConfigBaseView, BaseListView):
    # template_name = "config/list_configs.html"

    def get_queryset(self) -> QuerySet[Any]:
        return ReceiverConfiguration.objects.filter(user=self.request.user).order_by(
            "-id"
        )
