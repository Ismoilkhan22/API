from django.urls import path

from core.v1.auth import LoginView, RegisView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('regis/', RegisView.as_view()),

    path('regis/', RegisView.as_view()),
]

from core.v1.views import CategoryView, ProductView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ctgs', CategoryView, basename='ctg')
router.register(r'products', ProductView, basename='product')
urlpatterns = router.urls
