from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse_lazy

from MyBlog.accounts.models import Profile
from MyBlog.articles.models import Article

UserModel = get_user_model()


def create_profile(user):
    profile = Profile(
        user=user,
        first_name='Buby',
        last_name='Trifon',
        profile_image='image1.jpg',
    )
    profile.save()
    return profile


def create_articles_for_user(profile, count=5):
    result = []
    for i in range(count):
        article = Article(
            author=create_profile(profile),
            category='Courses',
            title=f'Title {i+1}',
            body=f'Body {i+1}',
            post_image=f'image {i+1}.jpg ',
            )
        article.save()
        result.append(article)
    return result


class UserDetailsViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'email': 'test@gmail.com',
            'password': 'password123',
        }

    def assertEmpty(self, collection):
        return self.assertEqual(0, len(collection), 'It is not empty')

    def _create_and_login_user(self, credentials):
        user = UserModel.objects.create_user(**credentials)
        self.client.login(**credentials)
        return user

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_and_login_user(self.credentials)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))
        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):

        user2 = self._create_and_login_user({
            'email': 'testttt@gmail.com',
            'password': '1password123',
        })
        user1 = self._create_and_login_user(self.credentials)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user2.pk}))
        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_no_article__expect_empty_list(self):
        user = self._create_and_login_user(self.credentials)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEmpty(response.context['user_article'])

    def test_user_details__when_1_article__expect_to_view_1_article(self):
        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)
        create_articles_for_user(profile.user, count=1)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(1, response.context['user_article_counts'])

    def test_user_details__when_two_articles__expect_two_articles_view(self):
        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)
        create_articles_for_user(profile.user, count=2)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(2, response.context['user_article_counts'])

    def test_user_details__when_four_articles_no_page__expect_four_articles_view(self):
        pass

    def test_user_details__when_four_articles_page_1__expect_four_articles_view(self):
        pass
        # user = self._create_and_login_user(self.credentials)
        # profile = create_profile(user)
        # articles = create_articles_for_user(profile.user, count=4)
        # response = self.client.get(
        #     reverse_lazy('details user', kwargs={'pk': user.pk}),
        #     data={
        #         'page': 1,
        #     })
        #
        # self.assertListEqual(articles, list(str(response.context['user_article_counts'])))
        #
        # self.assertEqual(4, response.context['user_article_counts'])

    def test_user_details__when_four_articles_page_2__expect_four_articles_view(self):
        pass
