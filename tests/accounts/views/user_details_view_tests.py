from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse

from MyBlog.accounts.models import Profile
from MyBlog.accounts.views import RegisterUserView

UserModel = get_user_model()


class UserDetailsViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.factory = RequestFactory()
        cls.user = UserModel.objects.create_user(email='test_user@gmail.com', password='secret123')


    def test_user_details_view__when_no_user__expect_empty_message(self):
        pass

    def test_user_details_view__when_user__expect_details_info(self):
        c = Client()
        # response = c.get('details user', {'first_name': 'fred', 'last_name': 'Trifon', 'profile_image': 'teddy.jpg'})
        # profile = [Profile(first_name='Teddy', last_name='Trifon', profile_image='teddy.jpg', user=self.user.id)]
        # Profile.objects.create(profile)
        # response = self.client.get(reverse('details user'))
        # # request = self.factory.get(profile)
        # profile.user = self.user.id
        print(self.factory)
        print(self.client)
        print(c)
        # self.assertEqual(RegisterUserView.as_view(response).status_code, 200)