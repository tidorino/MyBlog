from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy

from MyBlog.accounts.forms import RegisterUserForm

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/home-no-profile.html'
    form_class = RegisterUserForm

    success_url = reverse_lazy('index')

    # this is necessary for redirect to 'index' not to 'log in' page after register
    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class LogInView(auth_views.LoginView):
    template_name = 'accounts/login.html'

    # this success_url works as in setting.py we add LOGIN_URL = reverse_lazy('index')
    success_url = reverse_lazy('index')


class LogOutView(auth_views.LogoutView):

    #  Override next_page of  def get_default_redirect_url from LogoutView or
    # I can add in setting.py we add LOGOUT_URL = reverse_lazy('index')
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):

    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object

        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = (UserModel.USERNAME_FIELD, 'first_name', 'last_name', 'profile_image', )
    # form_class = EditUserForm

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
