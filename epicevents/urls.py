from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.users.urls')),
    path('', include('app.clients.urls')),
    path('', include('app.contracts.urls')),
    path('', include('app.events.urls'))
]
