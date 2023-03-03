from django.contrib.auth import get_user_model
from django.test import TestCase

from MyBlog.accounts.models import Profile

UserModel = get_user_model()


class ProfileModelTests(TestCase):

    # FIRST_NAME = 'Teodora'
    # LAST_NAME = 'Ivanov'
    # PROFILE_IMAGE = 'profile.jpg'
    #
    # @classmethod
    # def setUpTestData(cls):
    #     UserModel.objects.create()
    #
    def setUp(self):
        self.user = UserModel.objects.create(email='test_user@gmail.com', password='secret123')
        # profile = UserModel.objects.last().profile
        # self.profile = Profile(profile, self.FIRST_NAME, self.LAST_NAME, self.PROFILE_IMAGE)

    def test_profile_save__when_first_name_only_letters__expect_correct_result(self):
        pass

        # profile = Profile.objects.create(
        #     user=self.user, first_name='Teddy', last_name='Trifon', profile_image='teddy.jpg'
        # )
        # # Act
        # profile.full_clean()
        # profile.save()
        #
        # # Assert
        # self.assertIsNotNone(profile.pk)

    def test_profile_save__when_first_name_not_only_letters__expect_to_raise(self):
        pass

    def test_profile_save__when_last_name_only_letters__expect_correct_result(self):
        pass

    def test_profile_save__when_last_name_not_only_letters__expect_to_raise(self):
        pass

    def test_str_representation_of_profile(self):
        pass
        # user = UserModel.objects.create(email='test_user@gmail.com', password='secret123')
        # profile = Profile.objects.create(
        #     first_name='Teddy', last_name='Trifon', profile_image='teddy.jpg', user_id=self.user.id)
        #
        # self.assertEqual('Teddy Trifon', str(profile.fullname))
