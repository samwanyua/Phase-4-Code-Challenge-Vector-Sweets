from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Sweet(db.Model, SerializerMixin):
    __tablename__ = 'sweets'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    vendor_sweets = db.relationship("VendorSweet", back_populates="sweet", lazy="dynamic")

    def __repr__(self):
        return f'<Sweet {self.name}>'

class Vendor(db.Model, SerializerMixin):
    __tablename__ = 'vendors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    vendor_sweets = db.relationship("VendorSweet", back_populates="vendor", lazy="dynamic")

    def __repr__(self):
        return f'<Vendor {self.name}>'

class VendorSweet(db.Model, SerializerMixin):
    __tablename__ = 'vendor_sweets'

    id = Column(Integer, primary_key=True)
    price = Column(Integer, nullable=False)

    vendor_id = Column(Integer, ForeignKey('vendors.id'))
    sweet_id = Column(Integer, ForeignKey('sweets.id'))

    vendor = relationship("Vendor", back_populates="vendor_sweets")
    sweet = relationship("Sweet", back_populates="vendor_sweets")

    @validates('price')
    def validate_price(self, key, value):
        if value is None:
            raise ValueError("Price must have a value")
        if value < 0:
            raise ValueError("Price cannot be a negative number")
        return value

    def __repr__(self):
        return f'<VendorSweet {self.id}>'
