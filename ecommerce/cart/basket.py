from store.models import Product
from decimal import Decimal

class Basket:
    def __init__(self, req):
        self.session = req.session

        # The store starts off as empty because the user has added nothing
        if 'skey' in req.session:
            basket = self.session.get('skey')
        else:
            basket = self.session['skey'] = {}
        self.basket = basket

    # Returns the quantity of all items
    def __len__(self):
        return sum(item['quantity'] for item in self.basket.values())

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in = product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item


    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] = self.basket[product_id]['quantity'] + quantity
            self.session.modified = True
        else:
            self.basket[product_id] = {'price': str(product.regular_price), 'quantity': quantity}
            self.session.modified = True


    def delete(self, product):
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.session.modified = True


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())

    def get_price_with_shipment(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.basket.values())


    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['quantity'] = quantity
        self.session.modified = True

    def basket_update_delivery(self, delivery_price = 0):
        return self.get_price_with_shipment() + Decimal(delivery_price)























