"""styleshare_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path, include

from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # Admin Page
    path('admin/', admin.site.urls),

    # Restful API
    re_path(r'^goods/', include('goods.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        # Docs
        re_path(r'^docs/', include_docs_urls(
            title='StyleShare Django API',
            authentication_classes=[],
            permission_classes=[]
        )),
        # Django Debug Toolbar
        path('__debug__/', include(debug_toolbar.urls)),
    ]

