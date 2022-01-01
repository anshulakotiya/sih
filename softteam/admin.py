from django.contrib import admin
# Register your models here.

from .models import first_user, detail_of_worker, photo,attendence,attends,work,State,District
admin.site.register(first_user)
admin.site.register(detail_of_worker)
admin.site.register(photo)
admin.site.register(attendence)
admin.site.register(attends)
admin.site.register(work)
admin.site.register(State)
admin.site.register(District)


