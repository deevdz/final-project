from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import OrderLineItem
from products.models import Product
from checkout.models import Order


# Add product to the cart
# User must be logged in to view cart
# If product added to cart is a workshop check available spaces
@login_required(login_url='/accounts/login/')
def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_item, created = OrderLineItem.objects.get_or_create(
        item=item,
        user=request.user,
        purchased=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    print ('Type:' + str(item.product_type))
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            if (item.product_type != 'workshop'):
                order_item.quantity += 1
                order_item.save()
                messages.info(request, f"{item.title} quantity has updated.")
                return redirect("view_cart")
            elif (item.product_type == 'workshop') and (item.available_places <= order_item.quantity):
                messages.info(request,
                              f"There are not enough available places on this workshop - {item.title}")
                return redirect("view_cart")
            elif (item.product_type == 'workshop') and item.available_places > order_item.quantity:
                order_item.quantity += 1
                order_item.save()
                messages.info(request,
                              f"{item.title} quantity has updated.{item.available_places}")
                return redirect("view_cart")
        else:
            order.orderitems.add(order_item)
            messages.info(request, f"{item.title} has added to your cart.")
            return redirect("view_cart")
    else:
        order = Order.objects.create(
            user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, f"{item.title} has added to your cart.")
        return redirect("view_cart")


# Remove product from cart
@login_required(login_url='/accounts/login/')
def remove_from_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    cart_qs = OrderLineItem.objects.filter(user=request.user, item=item)
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
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = OrderLineItem.objects.filter(
                item=item,
                user=request.user,
            )[0]
            order.orderitems.remove(order_item)
            messages.warning(request, "This item was removed from your cart.")
            return redirect("view_cart")
        else:
            messages.warning(request, "This item was not in your cart")
            return redirect("view_cart")
    else:
        messages.warning(request, "You do not have an active order")
        return redirect("view_cart")


# Cart View - User must be registered to view cart
@login_required(login_url='/accounts/login/')
def view_cart(request):

    user = request.user

    carts = OrderLineItem.objects.filter(user=user, purchased=False)
    orders = Order.objects.filter(user=user, ordered=False)

    if carts.exists():
        if orders.exists():
            order = orders[0]
            return render(request,
                          'cart.html', {"carts": carts, 'order': order})
        else:
            messages.warning(request, "You do not have any item in your Cart")
            return render(request, "cart.html")
    else:
        messages.warning(request, "You do not have any item in your Cart")
        return render(request, "cart.html")


# Decrease the quantity of an item in the cart
@login_required(login_url='/accounts/login/')
def decrease_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item__slug=item.slug).exists():
            order_item = OrderLineItem.objects.filter(
                item=item,
                user=request.user
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request,
                                 f"{item.title} has removed from your cart.")
            messages.info(request,
                          f"{item.title} quantity has updated.")
            return redirect("view_cart")
        else:
            messages.info(request, f"{item.title} quantity has updated.")
            return redirect("view_cart")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("view_cart")
