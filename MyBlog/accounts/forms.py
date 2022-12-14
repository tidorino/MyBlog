from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView

from MyBlog.accounts.models import Profile

UserModel = get_user_model()


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    profile_image = forms.URLField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat password'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last name'})
        self.fields['profile_image'].widget.attrs.update({'placeholder': 'Profile image url'})

        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password1', 'password2', 'first_name', 'last_name', 'profile_image', )

    # save with data for profile
    def save(self, commit=True):
        user = super().save(commit=commit)
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        profile_image = self.cleaned_data['profile_image']

        profile = Profile(
            first_name=first_name,
            last_name=last_name,
            profile_image=profile_image,
            user=user,
        )
        if commit:
            profile.save()

        return user


class EditUserForm(UpdateView):

    model = Profile
    template_name = 'accounts/profile-edit-page.html'
    fields = '__all__'


class UserDeleteView(DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')




