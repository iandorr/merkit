from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdminMixin

from plugins_app.models import WelcomeModel,MainInfoModel,ContactFormModel, ServicesModel, ServiceModel, ServiceDetailModel

# Register your models here.

admin.site.register(WelcomeModel)
admin.site.register(MainInfoModel)

class ServicesAdmin(PlaceholderAdminMixin,admin.ModelAdmin):
    pass

class ServicesDetailAdmin(PlaceholderAdminMixin,admin.ModelAdmin):
    pass

admin.site.register(ServicesModel,ServicesAdmin)
admin.site.register(ServiceModel)
admin.site.register(ContactFormModel)
admin.site.register(ServiceDetailModel,ServicesDetailAdmin)