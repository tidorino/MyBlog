from MyBlog.accounts.models import Profile
from MyBlog.articles.models import Article, Category


def create_profile(user):
    profile = Profile(
        user=user,
        first_name='Buby',
        last_name='Trifon',
        profile_image='image1.jpg',
    )
    profile.save()
    return profile


def created_articles_for_user(profile, count=5):
    result = []
    category = create_category()

    for i in range(count):
        article = Article(
            author=create_profile(profile),
            category=category,
            title=f'Title {i+1}',
            body=f'Body {i+1}',
            post_image=f'image {i+1}.jpg ',
            )
        article.save()
        result.append(article)
    return result


def create_article(profile, category):
    article = Article(
        author=create_profile(profile),
        category=category,
        title='Title',
        body='Body',
        post_image='image.jpg',
    )
    article.save()
    return article


def create_category(name='Courses'):
    category = Category(name=name)
    category.save()
    return category
