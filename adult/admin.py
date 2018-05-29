from django.contrib import admin
from adult.models import * 
# Register your models here.

class CustAdult(admin.ModelAdmin):
	list_display=('age','workclass','fnlwgt','education','education_num','marital_status','occupation','relationship','race','sex','capital_gain','capital_loss','hours_per_week','native_country')
	list_filter=('sex','race','relationship')
admin.site.register(adult,CustAdult)
admin.site.register(WorkClass)
admin.site.register(Education)
admin.site.register(MartialStatus)
admin.site.register(Occupation)
admin.site.register(Relationship)
admin.site.register(Race)
admin.site.register(Sex)
admin.site.register(NativeCountry)