from home.models import HomePage
from wagtail.core.models import Page

def menuitems(context):
    try:
        home = HomePage.objects.first()
        children = home.get_children().filter(
            live=True,
            show_in_menus=True
        )
        list_children = [item for item in children]
        menuitems = [home] + list_children if home.show_in_menus and home.live else list_children
    except Exception as e:
        menuitems = []

    return {'menuitems': menuitems}
