from pyserver_getcheesy.views import (
    ListsAllView,
    CheesyQuoteCreateView,
    CheesyQuoteDeleteView,
    CheesyQuoteListView,
    CheesyQuoteUpdateView,
    CheesyJokeDetailView,
    CheesyJokeCreateView,
    CheesyJokeDeleteView,
    CheesyJokeListView,
    CheesyJokeUpdateView,
    CheesyJokeDetailView,
    ComplimentCreateView,
    ComplimentDeleteView,
    ComplimentListView,
    ComplimentUpdateView,
    ComplimentDetailView,
    ReceiverConfigurationCreateView,
    ReceiverConfigurationDeleteView,
    ReceiverConfigurationListView,
    ReceiverConfigurationUpdateView,
    ReceiverConfigurationDetailView,
    RandomComplimentView,
    RandomJokeView,
    RandomQuoteView,
    ChooseRandomView,
)

from django.urls import path, include


urlpatterns = [
    path("", ChooseRandomView.as_view(), name="redirect-home"),
    path("home/", ListsAllView.as_view(), name="home"),
    path("choose-random/", ChooseRandomView.as_view(), name="choose-random"),
    path("list-all/", ListsAllView.as_view(), name="list-all"),
    path("list-quotes/", CheesyQuoteListView.as_view(), name="list-quotes"),
    path("create-quote/", CheesyQuoteCreateView.as_view(), name="create-quote"),
    path(
        "update-quote/<int:pk>/", CheesyQuoteUpdateView.as_view(), name="update-quote"
    ),
    path(
        "delete-quote/<int:pk>/", CheesyQuoteDeleteView.as_view(), name="delete-quote"
    ),
    path("detail-quote/<int:pk>/", CheesyJokeDetailView.as_view(), name="detail-quote"),
    path("random-quote/", RandomQuoteView.as_view(), name="random-quote"),
    path("list-jokes/", CheesyJokeListView.as_view(), name="list-jokes"),
    path("create-joke/", CheesyJokeCreateView.as_view(), name="create-joke"),
    path("update-joke/<int:pk>/", CheesyJokeUpdateView.as_view(), name="update-joke"),
    path("delete-joke/<int:pk>/", CheesyJokeDeleteView.as_view(), name="delete-joke"),
    path("detail-joke/<int:pk>/", CheesyJokeDetailView.as_view(), name="detail-joke"),
    path("random-joke/", RandomJokeView.as_view(), name="random-joke"),
    path("list-compliments/", ComplimentListView.as_view(), name="list-compliments"),
    path(
        "create-compliment/", ComplimentCreateView.as_view(), name="create-compliment"
    ),
    path(
        "update-compliment/<int:pk>/",
        ComplimentUpdateView.as_view(),
        name="update-compliment",
    ),
    path(
        "delete-compliment/<int:pk>/",
        ComplimentDeleteView.as_view(),
        name="delete-compliment",
    ),
    path(
        "detail-compliment/<int:pk>/",
        ComplimentDetailView.as_view(),
        name="detail-compliment",
    ),
    path(
        "random-compliment/", RandomComplimentView.as_view(), name="random-compliment"
    ),
    path(
        "list-receiver-configs/",
        ReceiverConfigurationListView.as_view(),
        name="list-receiver-configs",
    ),
    path(
        "create-receiver-config/",
        ReceiverConfigurationCreateView.as_view(),
        name="create-receiver-config",
    ),
    path(
        "update-receiver-config/<int:pk>/",
        ReceiverConfigurationUpdateView.as_view(),
        name="update-receiver-config",
    ),
    path(
        "delete-receiver-config/<int:pk>/",
        ReceiverConfigurationDeleteView.as_view(),
        name="delete-receiver-config",
    ),
    path(
        "detail-receiver-config/<int:pk>/",
        ReceiverConfigurationDetailView.as_view(),
        name="detail-receiver-config",
    ),
]
