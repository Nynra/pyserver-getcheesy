from pyserver_getcheesy.models import (
    CheesyJoke,
    CheesyQuote,
    Compliment,
    ReceiverConfiguration,
)
from users.models import CustomUser as User

# from rest_framework.test import APITestCase
from django.utils import timezone
import datetime
from django.urls import reverse
from django.test import TestCase
from .utils import add_objects


class BaseRamdomizableModelTestCase:
    model_class = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if cls.model_class is None:
            raise NotImplementedError("model_class is None")

    def setUp(self):
        super().setUp()
        # Create a user
        self.sender = User.objects.create_user(
            username="testuser",
            nickname="testnickname",
            password="testpassword",
            email="testuser@test.com",
        )
        self.receiver = User.objects.create_user(
            username="testuser2",
            nickname="testnickname2",
            password="testpassword2",
            email="testuser2@test.com",
        )

    def test_get_random_index(self):
        """Test that _get_random_index returns a random index."""
        n = 10
        objects = add_objects(self.model_class, n, self.sender, self.receiver)
        index_list = [0 for i in range(n)]
        for i in range(1000):
            index = self.model_class._get_random_index(n)
            index_list[index] += 1

        # Check that all indices are used
        for i in range(n):
            self.assertGreater(index_list[i], 0)
            self.assertLess(index_list[i], 1000)

    def test_get_random_content_available(self):
        """Test that get_random returns a random object."""
        # Create some objects
        model_list = add_objects(self.model_class, 10, self.sender, self.receiver)
        id_list = [model.id for model in model_list]

        n = len(model_list)
        for i in range(n):
            # Get a random object
            model = self.model_class.get_random(user=self.receiver)
            # Check that the object is not None
            self.assertIsNotNone(model)
            # Check that the object is in the list
            self.assertIn(model.id, id_list)
            # Remove the id from the list to make sure repeating objects fail
            id_list.remove(model.id)
            # Check that the object is active
            self.assertTrue(model.is_active)

    def test_get_random_content_not_available(self):
        """Test that get_random returns None if no object is available."""
        model = self.model_class.get_random(user=self.receiver)
        self.assertIsNone(model)


class TestCheesyJoke(BaseRamdomizableModelTestCase, TestCase):
    model_class = CheesyJoke


class TestCheesyQuote(BaseRamdomizableModelTestCase, TestCase):
    model_class = CheesyQuote


class TestCompliment(BaseRamdomizableModelTestCase, TestCase):
    model_class = Compliment
