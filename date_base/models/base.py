from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import declared_attr
metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",

    }
)


@as_declarative(metadata=metadata)
class Base(object):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    __allow_unapped__= False





