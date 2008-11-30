# urls.py

from django.conf.urls.defaults import *

urlpatterns = patterns("ibake",
    (r"^$", "main.views.main"),
    (r"^main2", "main.views.main2"),
    (r"^foo", "green.views.foo"),
)
