from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class TestCaseBase(TestCase):
    def assertEmpty(self, collection):
        self.assertEqual(0, len(collection), 'It is not empty')

    def _create_and_login_user(self, credentials):
        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)
        return user
