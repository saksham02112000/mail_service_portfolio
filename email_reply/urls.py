from django.urls import path

# from . import views
from email_reply.views import *


urlpatterns = [
    path('portfolio_form/', portfolio_mail_reply),
    path('celeryTesting', celeryTest)
]