from app import app, db
from app import routers
from app.models.base import BaseModel

BaseModel.set_session(db.session)