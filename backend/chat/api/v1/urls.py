from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ThreadViewSet, ThreadActionViewSet, ThreadMemberViewSet

router = DefaultRouter()
router.register("thread", ThreadViewSet)
router.register("threadmember", ThreadMemberViewSet)
router.register("threadaction", ThreadActionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
