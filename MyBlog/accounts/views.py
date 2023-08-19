from django.core.paginator import Paginator
from django.views import generic as views
from django.contrib.auth import views as auth_views, login, get_user_model
from django.urls import reverse_lazy

from MyBlog.accounts.forms import RegisterUserForm
from MyBlog.accounts.models import Profile
from MyBlog.articles.models import Article

UserModel = get_user_model()


class RegisterUserView(views.CreateView):
    template_name = 'accounts/home-no-profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        login(request, self.object)
        return response


class LogInUserView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogOutUserView(auth_views.LogoutView):

    #  Override next_page of  def get_default_redirect_url from LogoutView or
    # I can add in setting.py  LOGOUT_URL = reverse_lazy('index')
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):

    template_name = 'accounts/profile-details-page.html'
    model = UserModel
    articles_paginate_by = 3

    def get_articles_page(self):
        return self.request.GET.get('page', 1)

    def get_paginated_articles(self):
        page = self.get_articles_page()
        articles = self.object.profile.articles.all()
        paginator = Paginator(articles, self.articles_paginate_by)
        return paginator.get_page(page)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 'self.object' is pk selected obj., 'self.req.user' is login obj.
        context['is_owner'] = self.request.user == self.object
        user_article = Article.objects.filter(author__user_id=self.object.pk)
        user_article_counts = user_article.count()
        context['user_article'] = user_article
        context['user_article_counts'] = user_article_counts

        context['page_object'] = self.get_paginated_articles()
        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = Profile
    fields = ('first_name', 'last_name')

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
