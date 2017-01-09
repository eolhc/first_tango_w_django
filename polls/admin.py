from django.contrib import admin



# Register your models here.
#Just one thing to do: we need to tell the admin that
# Question objects have an admin interface

from .models import Question

admin.site.register(Question)
