# class Category(db.Model):
#     name = db.Column(db.String(45), primary_key=True)
#
#
# class Characteristic(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     width = db.Column(db.Float, nullable=False)
#     length = db.Column(db.Float, nullable=False)
#     weight = db.Column(db.Float, nullable=False)
#
#
# class DeliveryType(db.Model):
#     type = db.Column(db.String(45), primary_key=True)
#
#
# class Delivery(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     price = db.Column(db.Float, nullable=False)
#     delivery_type_type = db.Column(db.String(45), db.ForeignKey('delivery_type.type'), nullable=False)
#     delivery_type = db.relationship('DeliveryType', backref='deliveries')
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_name = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(255), unique=True, nullable=False)
#     password = db.Column(db.String(100), nullable=False)
#     create_time = db.Column(db.TIMESTAMP, nullable=False)
#
#
# class Basket(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#
#
# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(45), nullable=False)
#     description = db.Column(db.String(500), nullable=False)
#     price = db.Column(db.Float, nullable=False)
#     characteristic_id = db.Column(db.Integer, db.ForeignKey('characteristic.id'), nullable=False)
#     category_name = db.Column(db.String(45), db.ForeignKey('category.name'), nullable=False)
#     characteristic = db.relationship('Characteristic', backref='products')
#     category = db.relationship('Category', backref='products')
#
#
# class BasketHasProduct(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#
#
# class Image(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     image = db.Column(db.String(100), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#
#
# class Order(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     date = db.Column(db.DateTime, nullable=False)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'), nullable=False)
#     user = db.relationship('User', backref='orders')
#     delivery = db.relationship('Delivery', backref='orders')
#
#
# class OrderHasBasket(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'), nullable=False)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
#
#
# class Review(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     response = db.Column(db.String(500))
#     product = db.relationship('Product', backref='reviews')
