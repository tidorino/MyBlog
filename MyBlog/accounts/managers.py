from django.contrib.auth import base_user
from django.contrib.auth.hashers import make_password


class BlogUserManager(base_user.BaseUserManager):
    # use_in_migrations = True

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError("You must provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        # user.password = make_password(password)
        user.set_password(password)
        user.is_active = True
        # user.save(using=self._db)

        user.save()

        return user

    # def create_user(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", False)
    #     extra_fields.setdefault("is_superuser", False)
    #     return self._create_user(email, password, **extra_fields)


