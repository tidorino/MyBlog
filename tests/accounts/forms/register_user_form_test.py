from django.test import TestCase

from MyBlog.accounts.forms import RegisterUserForm


class RegisterUserFormTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.form_data = {
            'email': 'test@gmail.com',
            'password1': 'isthislongenough',
            'password2': 'isthislongenough',
            'first_name': 'Buby',
            'last_name': 'Trifon',
            'profile_image': 'image1.jpg',
        }

    def test_register_user_form_empty_form(self):
        form = RegisterUserForm()

        self.assertIn('email', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('profile_image', form.fields)

    def test_register_user_form_if_placeholders_exist(self):
        form = RegisterUserForm()

        self.assertIn('placeholder="Email"', form.as_p())
        self.assertIn('placeholder="Password"', form.as_p())
        self.assertIn('placeholder="Repeat password"', form.as_p())
        self.assertIn('placeholder="First name"', form.as_p())
        self.assertIn('placeholder="Last name"', form.as_p())
        self.assertIn('placeholder="Profile image"', form.as_p())

    def test_register_user_form__is_valid(self):
        form = RegisterUserForm(self.form_data)

        self.assertTrue(form.is_valid())

    def test_register_user_form__when_password_help_text_is_none(self):
        form = RegisterUserForm(self.form_data)

        self.assertEqual(form.fields['password1'].help_text, None)
        self.assertEqual(form.fields['password2'].help_text, None)






