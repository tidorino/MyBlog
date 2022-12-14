from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from MyBlog.accounts.forms import RegisterUserForm
from MyBlog.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class BlogUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login', 'is_staff', 'is_superuser']
    list_filter = ()
    search_fields = ('email',)
    add_form = RegisterUserForm

    # additional fields for 'blog user' ,appear when add blog user
    add_fieldsets = (
        (
            'LogIn info',
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
        (
            'Profile info',
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "profile_image"),
            },
        ),
    )

    # permission fields for 'blog user', appear when click on 'email'
    fieldsets = (
        (None,
         {
             'fields': (
                 'email',
                 'password')}),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                    'groups',
                    'user_permissions',
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

