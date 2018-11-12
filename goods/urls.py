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
	re_path(r'^goods/$', views.GoodsListAPI.as_view()),
	re_path(r'^goods/(?P<pk>[0-9]+)/$', views.GoodsRetrieveAPI.as_view()),
	re_path(r'^', include(router.urls)),
]
