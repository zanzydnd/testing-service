from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin,
    UserManager as DjangoUserManager,
)


# Create your models here.

class UserManager(DjangoUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        user = self.model(email=email, username=username, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class ServiceUser(AbstractBaseUser, PermissionsMixin):
    object = UserManager()

    email = models.EmailField(unique=True, null=False)
    username = models.CharField(max_length=30, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password"]

    @property
    def is_staff(self):
        return self.is_superuser


class Meta:
    db_table = "ServiceUser"
    verbose_name = "Пользователь"
    verbose_name_plural = "Пользователи"


class Test(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "Test"
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class Question(models.Model):
    text = models.CharField(max_length=100)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name="questions")

    class Meta:
        db_table = "Question"
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    text = models.CharField(max_length=100)
    is_right = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="possible_answers")

    class Meta:
        db_table = "PossibleAnswers"
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"


class UserAnswers(models.Model):
    chosen_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)

    class Meta:
        db_table = "UserAnswers"
        verbose_name = "Выбранный ответ"
        verbose_name_plural = "Выбранные ответы"
