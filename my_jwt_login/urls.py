from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('api/my_jwt_login_app/', include('my_jwt_login_app.urls')),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/custom-token/',MyTokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view())   #not mandatory
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)