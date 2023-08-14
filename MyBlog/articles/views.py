from django.contrib.auth import get_user_model

from django.urls import reverse_lazy
from django.views import generic as views

from MyBlog.articles.forms import AddPostForm
from MyBlog.articles.models import Article


UserModel = get_user_model()


class DetailsPostView(views.DetailView):
    template_name = 'articles/details-post-page.html'
    model = Article


class AddPostView(views.CreateView):
    template_name = 'articles/add_post_page.html'
    model = Article
    form_class = AddPostForm

    success_url = reverse_lazy('index')


class EditPostView(views.UpdateView):
    template_name = 'articles/edit-post-page.html'
    model = Article
    fields = ('category', 'title', 'body', 'post_image')

    def get_success_url(self):
        return reverse_lazy(
            'details post',
            kwargs={
                'slug': self.kwargs.get('slug')
            },
        )


class DeletePostView(views.DeleteView):
    template_name = 'articles/delete-post-page.html'
    model = Article
    success_url = reverse_lazy('index')

# TODO -> https://stackoverflow.com/questions/65276895/querying-a-user-profile-model