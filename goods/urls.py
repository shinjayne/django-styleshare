# Outer Import
# rest framework
from rest_framework.routers import DefaultRouter
# django
from django.urls import path, re_path, include

# Inner Import
# views
from goods import views

router = DefaultRouter()
# router.register(r'profile', views.ProfileViewSet)

urlpatterns = [
	# url(r'^user/$', views.UserListCreate.as_view()),
	# url(r'^user/(?P<pk>[0-9]+)/$', views.UserRUD.as_view(), name='user-detail'),
	re_path(r'^', include(router.urls)),
]
