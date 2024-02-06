from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import registerView, CustomLoginView, CustomLogoutView, MainView, UserUpdateView, CartView, add_good_to_cart

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', registerView, name='register'),
    path('', MainView.as_view(), name='main'),
    path('profile/<int:pk>/', UserUpdateView.as_view(), name='profile'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add_good/<int:pk>', add_good_to_cart, name='add_good')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
