from django.urls import reverse_lazy, reverse

from tests.utils.creation_utils import create_profile
from tests.accounts.views.BaseTestCase import TestCaseBase


class UserEditViewTests(TestCaseBase):
    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'email': 'test@gmail.com',
            'password': 'password123',
        }

    def test_edit_user__when_user_is_login(self):
        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)

        self.assertIsNotNone(profile)
        response = self.client.post(reverse('edit user', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['user'])
        self.assertEqual(response.status_code, 200)


