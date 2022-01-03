DEFAULT_DB = "default"  # this is the managed db for auth, users
PRISMA_DB = "prisma"  # this is the unmanaged db for TD models


class PrismaRouter:
    """
    A router to control db operations
    """

    def db_for_read(self, model, **hints):

        if not model._meta.managed:
            return PRISMA_DB
        return DEFAULT_DB

    def db_for_write(self, model, **hints):

        if not model._meta.managed:
            return PRISMA_DB
        return DEFAULT_DB

    def allow_relation(self, obj1, obj2, **hints):

        if not obj1._meta.managed and obj2._meta.managed:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):

        if db == PRISMA_DB:
            return False
        return True
