from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from MyBlog.accounts.models import Profile

UserModel = get_user_model()


class RegisterUserViewTest(TestCase):
    # def setUp(self):
    #     self.valid_user_data = {
    #         'email': 'testemail@gmail.com',
    #         'password1': 'password',
    #         'password2': 'password',
    #         'first name': 'first name',
    #         'last name': 'last name',
    #         'profile image': 'image.jpg'
    #     }

    def test_register_user__when_valid_data__expect_logged_in_user(self):
        credentials = {
            'email': 'test@gmail.com',
            'password': 'password',
        }
        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)

        profile_data = {
            'user': user,
            'first_name': 'first name',
            'last_name': 'last name',
            'profile_image': 'image.jpg',
        }

        response = self.client.post(reverse('register user'), data=profile_data)

        create_profile = Profile.objects.filter(**profile_data).get()
        self.assertIsNotNone(create_profile)
        self.assertEqual(response.status_code, 302)
        # print(create_profile)



        # self.assertEqual(response.status_code, 200)

    def test_index_view__when_logged_in_user__email_to_be_correct(self):
        credentials = {
            'email': 'test@gmail.com',
            'password': 'password',
        }
        UserModel.objects.create_user(**credentials)

        self.client.login(**credentials)
        response = self.client.get(reverse('details user'))
        print(response)

        self.assertEqual('test@gmail.com', response.context['email'])