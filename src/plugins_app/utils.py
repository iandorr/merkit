from plugins_app.models import LinkManager
from cms.models.pluginmodel import CMSPlugin



def get_link_manager():

    managers = LinkManager.objects.all().order_by('pk')

    if not managers.exists():
        link_manager = LinkManager(number=1)
        link_manager.save()

    for i in range(1,len(managers)):
        managers[i].delete()

    link_manager = managers[0]

    return link_manager

def link_href_taken(href,model):

    link_manager = get_link_manager()

    draft_plugs = []
    plugs = CMSPlugin.objects.all()

    for plug in plugs:
        if plug.placeholder.page.publisher_is_draft:
            draft_plugs.append(plug.pk)


    for f in link_manager._meta.get_fields():
        if f.one_to_many:
            items = f.related_model.objects.all()
            for item in items:
                if (item.link_href == href and item.pk != model.pk and item.pk in draft_plugs):
                    return True
    return False