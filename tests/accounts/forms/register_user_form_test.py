from django.test import TestCase

from MyBlog.accounts.forms import RegisterUserForm


class RegisterUserFormTest(TestCase):
    def setUp(self) -> None:
        self.form_data = {
            'email': 'test@gmail.com',
            'password1': 'isthislongenough',
            'password2': 'isthislongenough',
            'first_name': 'Buby',
            'last_name': 'Trifon',
            'profile_image': 'image1.jpg',
        }

    def test__empty_form(self):
        form = RegisterUserForm()

        self.assertIn('email', form.fields)
        self.assertIn('password1', form.fields)
        self.assertIn('password2', form.fields)
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('profile_image', form.fields)

    def test__if_placeholders_exist(self):
        form = RegisterUserForm()

        self.assertIn('placeholder="Email"', form.as_p())
        self.assertIn('placeholder="Password"', form.as_p())
        self.assertIn('placeholder="Repeat password"', form.as_p())
        self.assertIn('placeholder="First name"', form.as_p())
        self.assertIn('placeholder="Last name"', form.as_p())
        self.assertIn('placeholder="Profile image"', form.as_p())

    def test__form__is_valid(self):
        form = RegisterUserForm(self.form_data)
        self.assertTrue(form.is_valid())

    def test__when_password_help_text_is_none(self):
        form = RegisterUserForm(self.form_data)

        self.assertEqual(form.fields['password1'].help_text, None)
        self.assertEqual(form.fields['password2'].help_text, None)

    def test__when_username_already_exist(self):

        form_data1 = {
            'email': 'test@gmail.com',
            'password1': 'isthislongenough',
            'password2': 'isthislongenough',
            'first_name': 'Tedy',
            'last_name': 'Tooo',
            'profile_image': 'image2.jpg',
        }

        form = RegisterUserForm(self.form_data)
        form1 = RegisterUserForm(form_data1)
        print(form1.errors)
        self.assertTrue(form.is_valid())
        self.assertTrue(form1.is_valid())




