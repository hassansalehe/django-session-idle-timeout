# -*- coding: UTF-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r"^$", views.PingView.as_view(), name="django-session-idle-timeout_ping"),
]
