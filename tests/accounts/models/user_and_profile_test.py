from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from MyBlog.accounts.models import Profile
from MyBlog.core.validators import validate_only_letters

UserModel = get_user_model()


class TestBlogUserModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = UserModel.objects.create_user(email='test_user@gmail.com', password='secret123')

    def test__str_representation_of_user(self):
        expected_response = 'test_user@gmail.com'
        self.assertEqual(expected_response, str(self.user))


class ProfileModelTests(TestCase):
    def setUp(self) -> None:
        self.user = UserModel.objects.create(email='test_user@gmail.com', password='secret123')
        self.profile = Profile(
            user=self.user,
            first_name='Teddy',
            last_name='Tooo',
            profile_image='image.jpg',
        )

    def test_profile_creation(self):

        self.assertIsInstance(self.user.profile, Profile)

        # Call the save method of the user to activate the signal
        # again, and check that it doesn't try to create another
        # profile instance

        self.user.save()
        self.assertIsInstance(self.user.profile, Profile)

    def test_profile_save__when_first_name_only_letters__expect_correct_result(self):

        self.user.full_clean()
        self.assertEqual(self.profile.first_name, 'Teddy')

    def test_profile_save__when_first_name_not_only_letters__expect_to_raise(self):

        profile_first_name = 'Teddy22'
        self.profile.first_name = profile_first_name
        self.user.full_clean()

        with self.assertRaises(ValidationError) as context:
            validate_only_letters(self.profile.first_name)
        self.assertEqual(context.exception.message, 'Only letters are allowed')

    def test_profile_save__when_last_name_only_letters__expect_correct_result(self):

        self.user.full_clean()

        self.assertEqual(self.profile.last_name, 'Tooo')

    def test_profile_save__when_last_name_not_only_letters__expect_to_raise(self):
        profile_last_name = 'Tooo22'
        self.profile.last_name = profile_last_name
        self.user.full_clean()

        with self.assertRaises(ValidationError) as context:
            validate_only_letters(self.profile.last_name)
        self.assertEqual(context.exception.message, 'Only letters are allowed')

    def test_str_representation_of_profile(self):
        profile_full_name = 'Teddy Tooo'
        expected_response = profile_full_name
        self.assertEqual(expected_response, str(self.profile.full_name))

