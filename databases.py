from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from werkzeug.local import LocalProxy
from sqlalchemy.ext.declarative import declarative_base
import config

Base = declarative_base()
engine = create_engine(config.MySQLServerConfig.url, echo=False, pool_recycle=60)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = LocalProxy(Session)

