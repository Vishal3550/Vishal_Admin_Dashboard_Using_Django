from django.contrib import admin
from api.models import Company,Employee

# Register your models here.
admin.site.site_header = "Vishal Admin Dashboard"
admin.site.site_title = "Custom Admin Portal"
admin.site.index_title = "Welcome to the Custom Admin Interface"

class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location','type')
    search_fields=('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','Company')
    list_filter=('Company',)

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
