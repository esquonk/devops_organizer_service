from django.urls import path, include

from api.v1.router import api_urlpatterns as api_v1

urlpatterns = [
    path('api/v1/', include((api_v1, 'api.v1'), namespace='v1')),
]
