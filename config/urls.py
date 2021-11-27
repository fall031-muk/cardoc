from django.contrib                 import admin
from django.urls                    import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers         import DefaultRouter
from users.views                    import UserViewset
from tires.views                    import User_TireViewset


router = DefaultRouter(trailing_slash=False)
router.register('user', UserViewset, basename='user')
router.register('tire', User_TireViewset, basename='tire')

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]