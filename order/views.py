from django.shortcuts import render
from order.forms import OrderForm
from cart.cart import Cart
from order.models import OrderItem


def order_detail(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid:
            order = form.save()
            for item in cart:
                print(item['product'])
                print(item['price'])
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         quantity=item['quantity'],
                                         price=item['price'])
            cart.clear()
            new_order = order
            print('ZAKAZ',order.id)
            return render(request, 'order/thanks_order.html', {'order':new_order})
    else:
        form = OrderForm()
        return render(request, 'order/order_detail.html', {'form':form,
                                                           'cart':cart})


