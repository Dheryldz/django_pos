from django.urls import path, reverse_lazy
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView

app_name = "authentication"
urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path('accounts/register/', register_user, name="register"),
    path('accounts/logout/', LogoutView.as_view(next_page=reverse_lazy('authentication:login')), name="logout")
]
