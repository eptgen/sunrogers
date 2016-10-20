"""ebdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name="index"),
	url(r'^bub/$', views.bub, name="bub"),
	url(r'^bump/$', views.bump, name="bump"),
	url(r'^php/$', views.php, name="php"),
	url(r'^isfat/[a-z]+/$', views.isfat, name="isfat"),
	url(r'^crackdetector/$', views.cd, name="cd"),
	url(r'^mixtape/$', views.mixtape, name="mixtape"),
	url(r'^google503cd29fc95f3756.html$', views.verification, name="verification"),
	url(r'^favicon.ico$', views.favicon, name="favicon"),
	url(r'^entername/', include("name.urls", namespace="name")),
	url(r'^chat/', include("chat.urls", namespace="chat")),
	url(r'^blog/', include("blog.urls", namespace="blog")),
	url(r'^comic/', include("comic.urls", namespace="comic")),
	url(r'^arduino/', include("arduino.urls", namespace="arduino")),
	url(r'^classes/', include("classes.urls", namespace="classes")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + [
	url(r'^', views.do_404, name="do404"),
]


































