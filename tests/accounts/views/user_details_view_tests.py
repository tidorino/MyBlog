from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from MyBlog.articles.models import Category
from tests.utils.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_profile, created_articles_for_user, create_category

UserModel = get_user_model()


class UserDetailsViewTests(TestCaseBase):
    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'email': 'test@gmail.com',
            'password': 'password123',
        }

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
        created_articles_for_user(profile.user, count=1)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(1, response.context['user_article_counts'])

    def test_user_details__when_two_articles__expect_two_articles_view(self):
        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)
        created_articles_for_user(profile.user, count=2)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(2, len(response.context['user_article']))
        self.assertEqual(2, response.context['user_article_counts'])

    def test_pagination_is_three__expect_page_1_three_articles_view(self):
        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)
        articles = created_articles_for_user(profile.user, count=3)
        articles_on_page = 3

        response = self.client.get(
                reverse_lazy('details user', kwargs={'pk': user.pk}),
                data={
                    'page': 2,
                })

        """
        List(reversed(articles)) --> Article.objects.order_by('-created_on') !!!
        """
        self.assertListEqual(list(reversed(articles)), list(response.context['user_article']))
        self.assertTrue(response.context['page_object'])

        self.assertEqual(articles_on_page, len(response.context['user_article']))
        self.assertEqual(3, response.context['user_article_counts'])


