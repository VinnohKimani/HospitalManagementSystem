from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy


metadata = Metadata()

db = SQLAlchemy(metadata=MetaData())