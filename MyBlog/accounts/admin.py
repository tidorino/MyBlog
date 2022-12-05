from django.contrib import admin
from django.contrib.auth import admin as auth_admin, get_user_model

from MyBlog.accounts.forms import RegisterUserForm

UserModel = get_user_model()


@admin.register(UserModel)
class BlogUserAdmin(auth_admin.UserAdmin):
    ordering = ('email',)
    list_display = ['email', 'date_joined', 'last_login']
    list_filter = ()
    add_form = RegisterUserForm
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("first_name", "last_name", "profile_image"),
            },
        ),
    )
    # fieldsets = (
    #     (None, {"fields": ("email", "password")}),
    #     (
    #         "Permissions",
    #         {
    #             "fields": (
    #                 "is_staff",
    #                 "is_superuser",
    #                 "groups",
    #                 "user_permissions",
    #             ),
    #         },
    #     ),
    #     ("Important dates", {"fields": ("last_login", "date_joined")}),
    # )
    #
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )

