from django.urls import path
from .views import login_view, logout_view, registration_view, check_username

app_name = 'user'

urlpatterns = [
    # path("register/", register_view, name="register"),
    path("registration/", registration_view, name="registration"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout")
]

htmx_urlpatterns = [
    path('check_username/', check_username, name='check_username')
]

urlpatterns += htmx_urlpatterns