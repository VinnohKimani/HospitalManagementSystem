from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

# from flask_migrate import Migrate
# from app import app


naming_convention = {
    "pk": "pk_%(table_name)s",  # deifnes how to write the primary key
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",  # foreign key
    "ix": "ix_%(table_name)s_%(column_0_name)s",  # indexing (quicker look ups)
    "uq": "uq_%(table_name)s_%(column_0_name)s",  # unique
    "ck": "ck_%(table_name)s_%(constraint_name)s",  # check
}

metadata = MetaData(naming_convention=naming_convention)
db = SQLAlchemy(metadata=metadata)
