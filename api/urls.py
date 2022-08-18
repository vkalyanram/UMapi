from . import views
from django.urls import re_path

urlpatterns=[

re_path(r'^api/(?P<token_value>[\w.-]+)/', views.get_details,name='get_details')
]

