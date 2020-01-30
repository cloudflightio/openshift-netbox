"""
Override the Netbox urls.py for OAuth login
"""

from netbox.urls import *
from netbox.openshift_auth import LogoutView

urlpatterns = [
    path(r'logout/', LogoutView.as_view(), name='logout'),
] + urlpatterns + [
    path(r'oauth/', include('social_django.urls', namespace='social')),
]
