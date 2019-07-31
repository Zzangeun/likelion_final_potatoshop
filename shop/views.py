from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'shop/home.html')

def detail_1(request):
    return render(request, 'shop/detail_1.html')

def detail_2(request):
    return render(request, 'shop/detail_2.html')

def detail_3(request):
    return render(request, 'shop/detail_3.html')

@login_required
def adminpage(request):
    orders = Order.objects
    return render(request, 'shop/adminpage.html', {'orders':orders})

@login_required
def mypage(request):
    orders = Order.objects
    return render(request, 'shop/mypage.html', {'orders':orders})

# def order_new(request):
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.save()
#             return redirect('order_detail', order_id=order.pk)
#     else:
#         form = OrderForm()
#     return render(request, 'shop/order_new.html', {'form':form})

def order_save(request):
    order = Order()
    # order.writer = user_name
    order.product = request.GET['product']
    order.orderer = request.GET['orderer']
    order.postcode = request.GET['postcode']
    order.address = request.GET['address']
    order.phone1 = request.GET['phone1']
    order.phone2 = request.GET['phone2']
    order.email = request.GET['email']
    order.message = request.GET['message']
    order.created_date = timezone.datetime.now()
    order.price = potato_price['order.product']
    order.delivery_price = del_price['order.product']
    order.total_price = order.price + order.delivery_price
    order.save()
    return redirect('order_detail', order_id=order.pk)

def order_new(request):
    return render(request, 'shop/order_new.html')

def order_edit(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('order_detail', order_id=order.pk)
    else:
        form = OrderForm(instance=order)
    return render(request, 'shop/order_edit.html', {'form':form})

def order_delete(request, order_id):
    order = get_object_or_404(Order, pk = order_id)
    order.delete()
    return redirect('home')

def order_detail(request, order_id):
    order_detail = get_object_or_404(Order, pk=order_id)
    return render(request, 'shop/order_detail.html', {'order':order_detail})
