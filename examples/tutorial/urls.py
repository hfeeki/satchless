from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

from products.app import products_app

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(products_app.urls)),
)