"""
Override the Netbox urls.py for OAuth login
"""

from netbox.urls import *
from django.urls import path
from netbox.openshift_auth import LogoutView

_patterns = [
    path(r'logout/', LogoutView.as_view(), name='logout'),
] + _patterns + [
    path(r'oauth/', include('social_django.urls', namespace='social')),
]
