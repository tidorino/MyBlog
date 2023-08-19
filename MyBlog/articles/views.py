from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect

from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView

from MyBlog.articles.forms import AddPostForm
from MyBlog.articles.models import Article, ArticleLike

UserModel = get_user_model()


class DetailsPostView(DetailView):
    template_name = 'articles/details-post-page.html'
    model = Article


class AddPostView(CreateView):
    template_name = 'articles/add_post_page.html'
    model = Article
    form_class = AddPostForm

    success_url = reverse_lazy('index')


class EditPostView(UpdateView):
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


class DeletePostView(DeleteView):
    template_name = 'articles/delete-post-page.html'
    model = Article
    success_url = reverse_lazy('index')


def like(request, post_id):
    user = request.user
    post = Article.objects.get(id=post_id)
    current_likes = post.likes
    liked = ArticleLike.objects.filter(user=user, post=post).count()
    if not liked:
        liked = ArticleLike.objects.create(user=user, post=post)
        current_likes = current_likes + 1
    else:
        liked = ArticleLike.objects.filter(user=user, post=post).delete()
        current_likes = current_likes - 1

    post.likes = current_likes
    post.save()

    return HttpResponseRedirect(reverse('details post', args=[post.slug]))
