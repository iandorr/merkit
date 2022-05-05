from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from plugins_app.models import ServiceModel

@toolbar_pool.register
class PluginToolbar(CMSToolbar):
    
    watch_models = [ServiceModel]