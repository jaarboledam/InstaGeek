from django.contrib.auth.models import User
from django.test import TestCase

from followers.models import Relationship
from followers.utils import get_followers, get_following


class RelationshipTests(TestCase):

    USERS_PASSWORD = 'skywalker'

    def setUp(self):
        """
        Se ejecuta antes de cada test
        """
        self.user1 = User.objects.create_user("Luke", "skywalker@starwars.com", self.USERS_PASSWORD)
        self.user2 = User.objects.create_user("Anakin", "annie@starwars.com", self.USERS_PASSWORD)
        Relationship.objects.create(origin=self.user1, target=self.user2)

    def test_get_followers_returns_users_that_follow_a_given_user(self):
        followers = get_followers(self.user2)
        self.assertEqual([self.user1], followers)

    def test_get_following_returns_users_that_follows_a_given_user(self):
        following = get_following(self.user1)
        self.assertEqual([self.user2], following)
