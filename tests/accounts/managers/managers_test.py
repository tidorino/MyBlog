from django.contrib.auth import get_user_model
from django.test import TestCase


UserModel = get_user_model()


class TestCustomerUserManager(TestCase):
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

    def test_create_user_with_empty_email_raises_error(self):
        with self.assertRaises(ValueError) as context:
            UserModel.objects.create_user(email='', password='secret123')
        self.assertEqual(str(context.exception), 'The given email must be set')

