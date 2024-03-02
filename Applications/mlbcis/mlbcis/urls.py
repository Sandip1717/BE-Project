"""mlbcis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mlbcis import views

from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.index,name="index"),

    path('rdoctor',views.rdoctor),
    path('rparent',views.rparent),

    path('login',views.login),
    path('fpassword',views.fpassword),

    path('logout',views.logout,name="logout"),

    path('admih/',views.adminh,name="admin"),
    path('aprofile/',views.aprofile,name="aprofile"),
    path('amanageuser/',views.amanageuser,name="amanageuser"),
    path('amanageuser/selectrole',views.srole),
    path('amanageuser/deleteu',views.deleteu),
    path('aviewblog/',views.aviewblog,name="aviewblog"),
    path('aviewblog/addblog',views.addblog),
    path('aviewblog/vblog',views.vblog),


    path('parent/',views.parenth,name="parent"),
    path('pprofile/',views.pprofile,name="pprofile"),
    path('pcheckreport/',views.pcheckreport,name="pcheckreport"),
    path('pcheckreport/<int:vid>/',views.pvdetails),
    path('pappointment/',views.pappointment,name="pappointment"),
    path('pappointment/<int:vid>/',views.pvdetails),
    path('pappointment/paappointment',views.paappointment,),
    path('pviewblog/',views.pviewblog,name="pviewblog"),
    path('pviewblog/pvblog',views.pvblog),

    path('Doctor/',views.doctorh,name="doctor"),
    path('dprofile/',views.dprofile,name="dprofile"),
    path('dappointment/',views.dappointment,name="dappointment"),
    path('dappointment/<int:vid>/',views.dvdetails),
    path('dappointment/vdone',views.vdone),
    path('dviewblog/',views.dviewblog,name="dviewblog"),
    path('dviewblog/daddblog',views.daddblog),
    path('dviewblog/dvblog',views.dvblog),

    path('nurse/',views.nurseh,name="nurse"),
    path('nprofile/',views.nprofile,name="nprofile"),
    path('nviewchild/',views.nviewchild,name="nviewchild"),
    path('nviewchild/nrparent',views.nrparent),
    path('nappointment/',views.nappointment,name="nappointment"),
    path('nappointment/<int:vid>/',views.nvdetails),
    path('nappointment/naappointment',views.naappointment),
    path('nviewblog/',views.nviewblog,name="nviewblog"),
    path('nviewblog/naddblog',views.naddblog),
    path('nviewblog/nvblog',views.nvblog),


]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)