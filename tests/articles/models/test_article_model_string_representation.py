from tests.utils.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_profile, create_article


class ArticleModelTests(TestCaseBase):
    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'email': 'test@gmail.com',
            'password': 'password123',
        }

    def test_str_representation_of_article(self):
        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)
        article = create_article(profile.user)

        expected_response = f'Title|Buby Trifon'
        result_title = f'{article.title}|{article.author.full_name}'
        self.assertEqual(expected_response, str(result_title))

    def test_auto_creation_of_slug(self):
        user = self._create_and_login_user(self.credentials)
        profile = create_profile(user)
        article = create_article(profile.user)
        expected_response = f'title'
        result_slug = article.slug
        self.assertEqual(expected_response, str(result_slug))