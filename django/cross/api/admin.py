from django.contrib import admin
from .models import User, Faces, Visitors

admin.site.register(User)
admin.site.register(Faces)
admin.site.register(Visitors)