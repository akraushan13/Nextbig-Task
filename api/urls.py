from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView, ProductViewSet


router = DefaultRouter()
router.register('products', ProductViewSet, basename="products")

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path('', include(router.urls)),
]