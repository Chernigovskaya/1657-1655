from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, \
    DeleteView

from adminapp.mixin import BaseClassContextMixin
from basketapp.models import Basket
from ordersapp.forms import OrderItemsForm
from ordersapp.models import Order, OrderItem


class OrderList(ListView, BaseClassContextMixin):
    model = Order
    title = 'Geeksop | Список заказов'


class OrderCreate(CreateView, BaseClassContextMixin):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:list')
    title = 'Geeksop | Создание заказов'

    def get_context_data(self, **kwargs):
        context = super(OrderCreate, self).get_context_data()
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemsForm,
                                             extra=1)
        if self.request.POST:
            formset = OrderFormSet(self.request.POST)
        else:
            basket_item = Basket.objects.filter(user=self.request.user)
            if basket_item:
                OrderFormSet = inlineformset_factory(Order, OrderItem,
                                                     form=OrderItemsForm,
                                                     extra=basket_item.count())
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_item[num].product
                    form.initial['quantity'] = basket_item[num].quantity
                    form.initial['price'] = basket_item[num].product.price
                # basket_item.delete()
            else:
                formset = OrderFormSet()

        context['orderitems'] = formset
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        orderitems = context['orderitems']

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()

            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
            if self.object.get_total_cost() == 0:
                self.object.delete()
        return super(OrderCreate, self).form_valid(form)


class OrderUpdate(UpdateView, BaseClassContextMixin):



class OrderRead(DetailView, BaseClassContextMixin):
    pass


class OrderDelete(DeleteView, BaseClassContextMixin):
    pass


def order_forming_complete(request, pk):
    pass
