import graphene
import py2neo
from singledispatch import singledispatch


def get_column_doc(prop):
    return getattr(prop, 'doc', None)


def convert_py2neo_relationship(relationship, registry, origin_model):
    related_class = relationship.related_class
    if type(related_class) == str:
        module_name, _, class_name = related_class.rpartition(".")
        if not module_name:
            module_name = origin_model.__module__
        module = __import__(module_name, fromlist=".")
        related_class = getattr(module, class_name)

    def dynamic_type():
        _type = registry.get_type_for_model(related_class)
        if not _type:
            return None
        return graphene.Field(graphene.List(_type))

    return graphene.Dynamic(dynamic_type)


def convert_py2neo_property(prop, registry=None):
    return convert_py2neo_type(type(prop), prop, registry)


@singledispatch
def convert_py2neo_type(type, prop, registry=None):
    return graphene.String()


@convert_py2neo_type.register(py2neo.ogm.Property)
def convert_to_string(type, prop, registry=None):
    return graphene.String()
