# Outer Import
# django
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

import requests

# Inner Import

# Create your models here.


class UserManager(BaseUserManager):
	def create_user(self, username, password=None):
		if not username:
			raise ValueError('User must have an username')

		user = self.model(
			username=username,
		)

		if not password:
			raise ValueError('User must have an password')

		return user

	def create_superuser(self, username, password=None):

		user = self.create_user(
			username=username,
			password=password
		)

		user.is_superuser = True
		user.save()

		return user


class User(AbstractBaseUser, PermissionsMixin):
	# password - default
	# last_login - default
	# is_superuser - default
	# is_active - default

	username = models.CharField(
		verbose_name='username',
		max_length=30,
		unique=True,
		null=False,
		blank=False
	)
	date_joined = models.DateTimeField(
		verbose_name='Date Joined',
		auto_now_add=True
	)

	objects = UserManager()

	# 로그인에 사용되는 필드
	USERNAME_FIELD = 'username'

	# 필수 입력 필드 지정
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = 'Authentication User'
		# ordering = '-id'

	def __str__(self):
		return self.username

	@property
	def is_staff(self):
		return self.is_superuser

