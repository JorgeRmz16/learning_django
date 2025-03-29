from django.urls import path
from .views import *

# associate a name for this app
app_name = 'core'

urlpatterns = [
    # rute, view, name
    path('', first_view, name='first_view')
]