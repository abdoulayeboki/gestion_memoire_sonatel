
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Gestion Memoire API",
      default_version='v1',
   ),
)

urlpatterns = [
    path('administration/', include('administration.urls')),
    path('sujet/', include('sujet_module.urls')),
    path('admin/', admin.site.urls),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
