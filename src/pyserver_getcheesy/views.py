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
    PyserverBaseCreateView,
    PyserverBaseUpdateView,
    PyserverBaseDetailView,
    PyserverBaseListView,
    PyserverBaseDeleteView,
)
from pyserver_getcheesy.models import (
    CheesyQuote,
    CheesyJoke,
    Compliment,
    ReceiverConfiguration,
)
from pyserver_getcheesy.forms import (
    CheesyQuoteDetailForm,
    CheesyQuoteChangeForm,
    CheesyQuoteCreationForm,
    CheesyQuoteRandomForm,
    CheesyJokeDetailForm,
    CheesyJokeChangeForm,
    CheesyJokeCreationForm,
    CheesyJokeRandomForm,
    ComplimentDetailForm,
    ComplimentChangeForm,
    ComplimentCreationForm,
    ComplimentRandomForm,
    ReceiverConfigurationDetailForm,
    ReceiverConfigurationChangeForm,
    ReceiverConfigurationCreationForm,
)

logger = logging.getLogger(__name__)
from pyserver_tools.mixins import HasGroupPermissionMixin
from pyserver_getcheesy.conf import settings


class BaseRandomView(View):
    """Base view for showing a random model instance.

    This is a base class for showing a random model instance, it should be subclassed
    and not used directly. The subclass should set the following attributes:

    - template_name: The name of the template to render.
    - model_name: The name of the model.
    - random_view_name: The name of the random view.
    """

    template_name: str = "getcheesy/random_model.html"
    no_content_template_name: str = "getcheesy/no_content.html"
    model_name: str = None
    random_view_name: str = None

    def get(self, request, *args, **kwargs):
        model = self.model.get_random(user=self.request.user)
        if model is None:
            # Return no content available
            return render(request, self.no_content_template_name)

        model.update_activation_date()
        form = self.form_class(instance=model)
        logger.info("User {} got a random {}".format(request.user, str(model)))
        return render(request, self.template_name, self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
        except AttributeError:
            context = {}
        context["form"] = kwargs["form"]
        context["model_name"] = self.model_name
        context["random_item_url"] = self.random_view_name
        return context


# Create a create, update, delete and list view for each model
# Create a list all view that lists all the models
class ListsAllView(LoginRequiredMixin, HasGroupPermissionMixin, View):

    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CREATOR_GROUP_NAME,
        ]
    }
    template_name = "getcheesy/list_all.html"

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
        return render(request, self.template_name, context=context_data)

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

    template_name = "getcheesy/home.html"
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

    template_name = "getcheesy/choose_random.html"
    permission_groups = {
        "get": [
            settings.PYSERVER_GETCHEESY_ADMIN_GROUP_NAME,
            settings.PYSERVER_GETCHEESY_GETCHEESY_CONSUMER_GROUP_NAME,
        ]
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


# Logout redirect view
class LogoutRedirectView(LoginRequiredMixin, View):
    def get(self, request):
        return redirect("redirect-home")


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


class CheesyQuoteCreateView(
    CheesyQuoteBaseView,
    PyserverBaseCreateView,
):
    form_class = CheesyQuoteCreationForm


class CheesyQuoteUpdateView(CheesyQuoteBaseView, PyserverBaseUpdateView):
    form_class = CheesyQuoteChangeForm


class CheesyQuoteDeleteView(CheesyQuoteBaseView, PyserverBaseDeleteView):
    success_url = "list-quotes"


class CheesyQuoteDetailView(CheesyQuoteBaseView, PyserverBaseDetailView):
    form_class = CheesyQuoteDetailForm


# List views
class CheesyQuoteListView(CheesyQuoteBaseView, PyserverBaseListView):
    # template_name = "quote/list_quotes.html"
    pass


class RandomQuoteView(CheesyQuoteBaseView, BaseRandomView):
    form_class = CheesyQuoteRandomForm


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


class CheesyJokeCreateView(CheesyJokeBaseView, PyserverBaseCreateView):
    form_class = CheesyJokeCreationForm


class CheesyJokeUpdateView(CheesyJokeBaseView, PyserverBaseUpdateView):
    form_class = CheesyJokeChangeForm


class CheesyJokeDeleteView(CheesyJokeBaseView, PyserverBaseDeleteView):
    success_url = "list-jokes"


class CheesyJokeDetailView(CheesyJokeBaseView, PyserverBaseDetailView):
    form_class = CheesyJokeDetailForm


class CheesyJokeListView(CheesyJokeBaseView, PyserverBaseListView):
    pass


class RandomJokeView(CheesyJokeBaseView, BaseRandomView):
    form_class = CheesyJokeRandomForm


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


class ComplimentCreateView(ComplimentBaseView, PyserverBaseCreateView):
    form_class = ComplimentCreationForm


class ComplimentUpdateView(ComplimentBaseView, PyserverBaseUpdateView):
    form_class = ComplimentChangeForm


class ComplimentDeleteView(ComplimentBaseView, PyserverBaseDeleteView):
    success_url = "list-compliments"


class ComplimentDetailView(ComplimentBaseView, PyserverBaseDetailView):
    form_class = ComplimentDetailForm


class ComplimentListView(ComplimentBaseView, PyserverBaseListView):

    def get_queryset(self):
        return Compliment.objects.all()


class RandomComplimentView(ComplimentBaseView, BaseRandomView):
    form_class = ComplimentRandomForm


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


class ReceiverConfigurationCreateView(ReceiverConfigBaseView, View):
    form_class = ReceiverConfigurationCreationForm
    template_name = "tools_templates/create_model.html"

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
            "previous_page_url": self.request.META.get("HTTP_REFERER", "/"),
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


class ReceiverConfigurationUpdateView(ReceiverConfigBaseView, PyserverBaseUpdateView):
    form_class = ReceiverConfigurationChangeForm


class ReceiverConfigurationDeleteView(ReceiverConfigBaseView, DeleteView):
    template_name = "tools_templates/delete_model.html"
    success_url = "list-receiver-config"
    context_object_name = "item"

    def form_valid(self, form):
        # Check if the user field matches the request user
        if self.object.user != self.request.user:
            logger.error(
                f"User {self.request.user} tried to delete a receiver config that does not belong to them."
            )
            return self.form_invalid(form)
        return super().form_valid(form)

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
        context["previous_page_url"] = self.request.META.get("HTTP_REFERER", "/")
        return context


class ReceiverConfigurationDetailView(ReceiverConfigBaseView, PyserverBaseDetailView):
    form_class = ReceiverConfigurationDetailForm


class ReceiverConfigurationListView(ReceiverConfigBaseView, PyserverBaseListView):

    def get_queryset(self) -> QuerySet[Any]:
        return ReceiverConfiguration.objects.filter(user=self.request.user).order_by(
            "-id"
        )
