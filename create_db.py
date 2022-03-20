from app.models.users import Base
from app.db.session import engine

Base.metadata.create_all(engine)