from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ContactViewSet, ProfileViewSet, VerificationCodeViewSet

router = DefaultRouter()
router.register("profile", ProfileViewSet)
router.register("contact", ContactViewSet)
router.register("verificationcode", VerificationCodeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
