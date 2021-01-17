"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from notice.views import NoticeViewSet
from businesscard.views import BusinessCardViewSet
from businesscardbook.views import BusinessCardBookViewSet
from businesscardocr.views import BusinessCardOcrViewSet
from groupbusinesscard.views import GroupBusinessCardViewSet

router = routers.DefaultRouter()
router.register(r'notice', NoticeViewSet, 'notice')
router.register(r'businesscard', BusinessCardViewSet, 'businesscard')
router.register(r'businesscardbook', BusinessCardBookViewSet, 'businesscardbook')
router.register(r'businesscardocr', BusinessCardOcrViewSet, 'businesscardocr')
router.register(r'groupbusinesscard', GroupBusinessCardViewSet, 'groupbusinesscard')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls")),
    path('api/rest-auth/', include("rest_auth.urls")),
    path('api/rest-auth/registration/', include("rest_auth.registration.urls")),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)