from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm
# from geekshop.mixin import CustomDispatchMixin
from geekshop.mixin import CustomDispatchMixin
from users.models import User
from django.shortcuts import render
from products.models import ProductCategory, Product

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def index(request):
    return render(request,'admins/admin.html')


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    context_object_name = 'users'


    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(UserListView, self).get_context_data(**kwargs)
       context['title'] = 'Админка | Пользователи'
       return context


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(UserCreateView, self).get_context_data(**kwargs)
       context['title'] = 'Админка | Регистрация'
       return context


class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(UserUpdateView, self).get_context_data(**kwargs)
       context['title'] = 'Админка | Обновление пользователя'
       return context


class UserDeleteView(DeleteView, CustomDispatchMixin):

    model = User
    template_name = 'admins/admin-users-read.html'
    success_url = reverse_lazy('admins:admins_user')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch( request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-categories-read.html'
    context_object_name = 'categories'


    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(CategoryListView, self).get_context_data(**kwargs)
       context['title'] = 'Админка | Категории'
       return context


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-categories-create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(CategoryCreateView, self).get_context_data(**kwargs)
       context['title'] = 'Админка | Регистрация'
       return context


class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('admins:admins_category')

    def get_context_data(self, *, object_list=None, **kwargs):
       context = super(CategoryUpdateView, self).get_context_data(**kwargs)
       context['title'] = 'Админка | Обновление категории'
       return context


class CategoryDeleteView(DeleteView, CustomDispatchMixin):

    model = ProductCategory
    template_name = 'admins/admin-categories-update-delete.html'
    success_url = reverse_lazy('admins:admins_category')


class ProductCreateView(CreateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-create.html'
    fields = ['name', 'description', 'price', 'quantity', 'category']
    success_url = reverse_lazy('admins:admins_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка / Создание товара'
        return context


class ProductsListView(ListView):
    model = Product
    template_name = 'admins/admin-products-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка / Список товаров'
        return context


class ProductUpdateView(UpdateView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    fields = ['name', 'description', 'price', 'quantity', 'category']
    success_url = reverse_lazy('admins:admins_products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка / Обновление товара'
        return context


class ProductDeleteView(DeleteView, CustomDispatchMixin):
    model = Product
    template_name = 'admins/admin-products-update-delete.html'
    success_url = reverse_lazy('admins:admins_products')
