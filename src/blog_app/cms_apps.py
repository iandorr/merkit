from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool

class ArticleApp(CMSApp):
    name = ('Article')
    app_name = 'blog_app'

    def get_urls(self, page=None, language=None, **kwargs):
        return ["blog_app.urls"]

apphook_pool.register(ArticleApp)