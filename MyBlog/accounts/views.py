from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy

from MyBlog.accounts.forms import RegisterUserForm
from MyBlog.accounts.models import Profile

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    model = UserModel
    template_name = 'accounts/home-no-profile.html'
    form_class = RegisterUserForm

    success_url = reverse_lazy('index')

    # this is necessary for redirect to 'index' not to 'log in' page after register
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        result = super().form_valid(form)

        login(self.request, self.object)
        return result


class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogOutUserView(auth_views.LogoutView):

    #  Override next_page of  def get_default_redirect_url from LogoutView or
    # I can add in setting.py we add LOGOUT_URL = reverse_lazy('index')
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):

    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        # queryset = Article.objects.filter(status=1).order_by('-created_on')
        context = super().get_context_data(**kwargs)

        # 'self.object' is pk selected obj. , 'self.req.user' is login obj.
        context['is_owner'] = self.request.user == self.object
        # context['queryset'] = queryset
        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = Profile

    fields = ('first_name', 'last_name', 'profile_image', )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = Profile.objects.get(pk=self.object.user_id)
        return context

    # dynamic success url because of user.pk
    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
