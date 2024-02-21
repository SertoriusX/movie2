from django.contrib import admin
from .models import  movie,Tag_s,Tag,lastmovie,Contact

# Register your models here.
class postAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(movie,postAdmin)
admin.site.register(Tag)
admin.site.register(lastmovie,postAdmin)
admin.site.register(Tag_s)
admin.site.register(Contact)