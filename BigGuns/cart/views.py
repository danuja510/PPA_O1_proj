from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from django.contrib import messages
from .models import Cart, Order

def add_to_cart(request, id):
    item = get_object_or_404(Product, id=id)
    order_item, created = Cart.objects.get_or_create(
        item=item,
        user=request.user
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("store-home")
        else:
            order.orderitems.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("store-home")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("store-home")

# Remove item from cart

def remove_from_cart(request, id):
    item = get_object_or_404(Product, id=id)
    cart_qs = Cart.objects.filter(user=request.user, item=item)
    if cart_qs.exists():
        cart = cart_qs[0]
        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
        else:
            cart_qs.delete()
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("store-home")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("store-home")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("store-home")

# Cart View
def CartView(request):

    user = request.user

    carts = Cart.objects.filter(user=user, purchased=False)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        if orders.exists():
            order = orders[0]
            return render(request, 'cart/cart.html', {"carts": carts, 'order': order})
        else:
            messages.warning(request, "You do not have any item in your Cart")
            return redirect("store-home")
		
    else:
        messages.warning(request, "You do not have any item in your Cart")
        return redirect("store-home")


# Decrease the quantity of the cart :

def decreaseCart(request, id):
    item = get_object_or_404(Product, id= id)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__id=item.id).exists():
            order_item = Cart.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.title} has removed from your cart.")
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect("view-cart")
        else:
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect("view-cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("view-cart")