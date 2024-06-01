from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey, Integer, String, Boolean

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

Base = declarative_base()

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Vendor(db.Model):
    __tablename__ = 'Vendor'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50))
    discount = db.Column(Integer)
    active = db.Column(Boolean)

    products = db.relationship('Product', backref='vendor', lazy='dynamic')

    def __repr__(self) -> str:
        return 'Vendor: {}/{}'.format(self.id, self.name)


class Product(db.Model):
    __tablename__ = 'Product'
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(50))
    vendor_id = db.Column(Integer, ForeignKey('Vendor.id'))

    def __repr__(self) -> str:
        return 'Product: {}/{}'.format(self.id, self.name)


@app.route('/')
def index():
    db.create_all()

    # v1 = Vendor(id=1, name='Microsoft', discount=0,
    #             active=True)  # type: ignore
    # db.session.add(v1)
    # db.session.commit()
    vendors = Vendor.query.all()
    ret = ''
    for v in vendors:
        ret += str(v)+'<br>'
    return 'Hello<br>{}'.format(ret)


if __name__ == '__main__':
    app.run()
