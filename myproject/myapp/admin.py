from django.contrib import admin

# Register your models here.
from myapp.models import Statement
admin.site.register(Statement)
from myapp.models import Response
admin.site.register(Response)
