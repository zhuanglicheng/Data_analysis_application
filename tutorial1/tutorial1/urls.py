from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls import url, include
urlpatterns = [
    url(r'^', include('snippets.urls')),
    # url(r'^admin/', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-auth/', include('rest_framework.urls')),
]