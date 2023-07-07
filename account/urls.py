from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import register, login_page, logout_page

urlpatterns = [
    # Registration
    path("register/", register, name="register"),

    # Login and logout
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name="logout"),

    # Password reset
    path("password_reset/", PasswordResetView.as_view(template_name="account/password_reset.html", html_email_template_name="account/password_mail.html"), name="password_reset"),
    path("password_reset_done/", PasswordResetDoneView.as_view(template_name="account/password_reset_done.html"), name="password_reset_done"),
    path("password_reset_confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password_reset_complete/", PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name="password_reset_complete")
]