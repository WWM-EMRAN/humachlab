### Define different routers for different apps
class AllDBRouters:
    """
    A router to control database operations for emran and website apps.
    """
    def db_for_read(self, model, **hints):
        """Direct reads for emran and website models to their databases."""
        if model._meta.app_label == 'emran':
            return 'emran_db'
        elif model._meta.app_label == 'website':
            return 'website_db'
        return None

    def db_for_write(self, model, **hints):
        """Direct writes for emran and website models to their databases."""
        if model._meta.app_label == 'emran':
            return 'emran_db'
        elif model._meta.app_label == 'website':
            return 'website_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if the models are in the same database."""
        if obj1._meta.app_label == obj2._meta.app_label:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure the models migrate only to their respective databases."""
        if app_label == 'emran':
            return db == 'emran_db'
        elif app_label == 'website':
            return db == 'website_db'
        return None
