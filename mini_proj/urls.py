"""
URL configuration for mini_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Trading API",
        default_version='v1',
        description="API documentation for Trading App",
        terms_of_service="https://your-website.com/terms/",
        contact=openapi.Contact(email="contact@your-website.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

import notifications
import sales.urls, users.urls, analytics.urls, products.urls, trading.urls, notifications.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sales/', include(sales.urls)),
    path('users/', include(users.urls)),
    path('analytics/', include(analytics.urls)),
    path('products/', include(products.urls)),
    path('trading/', include(trading.urls)),
    path('notifications/', include(notifications.urls)),


    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Redoc UI (alternative)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Raw JSON API schema
    path('swagger.json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),

]
