from .views import UserListCreate, UserDetail
from django.urls import path, include

urlpatterns = [
    path('', UserListCreate.as_view(), name='user-list-create'),
    path('<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

