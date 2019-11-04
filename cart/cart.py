from _decimal import Decimal
from online_shop.settings import CART_SESSION_ID
from shop.models import Product
from .forms import CartAddProductForm


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, quantity=1, update_quantity=False):
        self.cart[product.id] = {}
        self.cart[product.id]['price'] = int(product.price)
        self.cart[product.id]['quantity'] = quantity
        self.cart[product.id]['update'] = update_quantity
        self.save()


    def save(self):
        self.session[CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Product.objects.filter(id__in=products_ids)
        for item in products:
            self.cart[str(item.id)]['product'] = item

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(item['quantity'] * item['price'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_ID]
        self.session.modified = True
