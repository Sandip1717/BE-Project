from django.contrib import admin

from childdata.models import Imagef
from childdata.models import Doctor
from childdata.models import Parent
from childdata.models import Blog
from childdata.models import Vaccine
from childdata.models import Vaccinereport

class ImagefAdmin(admin.ModelAdmin):
    list_display=('image',)
admin.site.register(Imagef,ImagefAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display=('fname','sname','photo','uname','epass','hname','haddress','mobile','nname','nphoto','nuname','nepass')
admin.site.register(Doctor,DoctorAdmin)

class ParentAdmin(admin.ModelAdmin):
    list_display=('fname','photo','address','mobile','cname','cdob','uname','hid','hname','epass')
admin.site.register(Parent,ParentAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display=('btitle','bphoto','bdata','bauthor','bdate')
admin.site.register(Blog,BlogAdmin)

class VaccineAdmin(admin.ModelAdmin):
    list_display=('age','days','vaccine','due','max','Dose','route','disease','symptoms','precautions')
admin.site.register(Vaccine,VaccineAdmin)

class VaccinereportAdmin(admin.ModelAdmin):
    list_display=('vid','age','vaccine','due','max','given','dose','route','disease','symptoms','precautions','cid','cname','cphoto','pname','did','dname','hname','height','weight','action')
admin.site.register(Vaccinereport,VaccinereportAdmin)
# Register your models here.