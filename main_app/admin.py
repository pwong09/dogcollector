from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Dog)
admin.site.register(Feeding)
admin.site.register(Toy)
admin.site.register(Photo)
admin.site.register(Profile)