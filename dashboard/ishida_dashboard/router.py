from django.conf import settings
class DatabaseAppsRouter:
    router_app_labels = {'auth','contenttypes','sessions', 'admin'}
   
    def db_for_read(self, model, **hints):
        """"Point all read operations to the specific database."""
        if model._meta.app_label in self.router_app_labels:
            return 'main'
        return None
    def allow_relation(self, obj1,obj2, **hints):
        if(
            obj1._meta.app_label in self.router_app_labels or
            obj2._meta.app_label in self.router_app_labels 
        ):
            return True
        return None
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.router_app_labels:
            return db == 'main'
        return None