from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ETS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
# ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ) + static(settings.STATIC_URL)
) + static(settings.STATIC_URL)
