from django.contrib import admin
from main.models import RepoInformation

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('name_project', 'all_repos', )

# Register your models here.
admin.site.register(RepoInformation, QuoteAdmin)