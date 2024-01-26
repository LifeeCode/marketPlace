from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import registerView, CustomLoginView, CustomLogoutView, MainView, UserUpdateView
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', registerView, name='register'),
    path('', MainView.as_view(), name='main'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
