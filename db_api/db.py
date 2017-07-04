from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy.ext.hybrid import hybrid_property
from databases import Base


class AP(Base):
    __tablename__ = 'ap'

    mac = Column(String, primary_key=True)
    _location = Column(String)
    vendor = Column(String)
    name = Column(String)
    ip = Column(String)
    address = Column(String)
    ac_ip = Column(String)
    online = Column(Integer)
    mpoi_id = Column(Integer)
    conns = Column(Integer)
    sens = Column(Integer, default=0)
    model = Column(String)
    ctime = Column(DateTime, default=text('CURRENT_TIMESTAMP'))
    mtime = Column(DateTime)

    def __repr__(self):
        return '<AP(mac={})>'.format(self.mac)

    # @hybrid_property
    # def ctime(self):
    #     return self.ctime.strftime("%Y-%m-%d %H:%M:%S")
    #
    # @hybrid_property
    # def mtime(self):
    #     return self.mtime.strftime("%Y-%m-%d %H:%M:%S")