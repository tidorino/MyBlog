from django.urls import reverse

from tests.utils.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_profile


class RegisterUserViewTest(TestCaseBase):
    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'email': 'test@gmail.com',
            'password': 'password123',
        }

    def test_register_user__when_valid_data__expect_logged_in_user(self):

        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)

        response = self.client.post(reverse('register user'))

        self.assertIsNotNone(profile)
        self.assertEqual(response.status_code, 200)


