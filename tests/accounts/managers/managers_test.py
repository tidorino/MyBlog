from django.contrib.auth import get_user_model
from django.test import TestCase


UserModel = get_user_model()


class TestCustomerUser(TestCase):
    @classmethod
    def setUpTestData(cls):

        cls.user = UserModel.objects.create_user(email='test_user@gmail.com', password='secret123')

    def test_create_user(self):
        self.assertIsInstance(self.user, UserModel)
        self.assertFalse(self.user.is_staff)
        self.assertEqual(self.user.email, 'test_user@gmail.com')

    def test_create_super_user(self):
        user = UserModel.objects.create_superuser(email='testt_user@gmail.com', password='secret123')
        self.assertIsInstance(user, UserModel)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'testt_user@gmail.com')

    def test__when_no_email_raise_error(self):

        self.assertRaises(ValueError, UserModel.objects.create_user, email='', password='secret123')
        with self.assertRaises(Exception) as ex:
            UserModel.objects.create_user(email='', password='secret123')
        self.assertEqual('The given email must be set', str(ex.exception))


