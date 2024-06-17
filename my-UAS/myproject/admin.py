from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(License)
admin.site.register(Course)