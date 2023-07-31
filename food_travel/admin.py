
from django.apps import apps
from django.contrib import admin

def register_all_models(app_name):
    app_models = apps.get_app_config(app_name).get_models()
    for model in app_models:
        try:
            admin.site.register(model)
        except admin.sites.AlreadyRegistered:
            pass

register_all_models('food_travel')
