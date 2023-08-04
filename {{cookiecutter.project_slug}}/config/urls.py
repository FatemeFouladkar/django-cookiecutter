from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    
    {% if cookiecutter.use_simple_jwt == 'y' %}
    #JWT tokens urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    {% endif %}
   
    {% if cookiecutter.use_django_rq == 'y' %}
    # Django-rq
    path('admin/rq/', include('django_rq.urls')),
    {% endif %}  

    {% if cookiecutter.use_drf == 'y' %}
    # API
    path('api/v1/', include('config.api', namespace='v1')),  
    {% else %}
    path('user/', include('users.urls')),
    {% endif %}
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)