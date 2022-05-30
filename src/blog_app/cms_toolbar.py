from cms.toolbar_base import CMSToolbar
from cms.toolbar_pool import toolbar_pool
from cms.toolbar.items import Break, SubMenu
from cms.cms_toolbar import ADMIN_MENU_IDENTIFIER, ADMINISTRATION_BREAK

@toolbar_pool.register
class ArticleAddToolbar(CMSToolbar):
    def populate(self):
        pass