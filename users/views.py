from django.contrib import messages, auth
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, UpdateView

from basket.models import Basket
from geekshop import settings
from geekshop.mixin import UserActiveCheckMixin, BaseClassContextMixin
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
# Create your views here.
from users.models import User


class LoginListView(LoginView, BaseClassContextMixin):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


class RegisterListView(FormView, BaseClassContextMixin):
    model = User
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    title = 'Регистрация'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verification_link(user):
                messages.success(request, 'Вы успешно зарегистрировались!')
            return redirect(self.success_url)
        messages.success(request, form.errors)
        return redirect(self.success_url)


class Logout(LogoutView, BaseClassContextMixin, UserActiveCheckMixin):
    template_name = 'products/index.html'


class ProfileFormView(UpdateView, UserActiveCheckMixin):
    model = User
    template_name = 'users/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data(**kwargs)
        context['title'] = 'Профиль'
        context['basket'] = Basket.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, files=request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные профиля успешно обновлены!')
            return redirect(self.success_url)
        messages.success(request, form.error_messages)
        return redirect(self.success_url)


def send_verification_link(user):
    link = reverse('users:verify', args=[user.email, user.activation_key])
    subject = f'Для активации профиля {user.username}, кликните по ссылке.'
    message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{link}'
    from django.core.mail import send_mail
    if settings.DEBUG:
        print(f'{settings.DOMAIN_NAME}{link}')
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user and user.activation_key == activation_key and not user.is_activation_key_expired():
            user.activation_key = ''
            user.activation_key_created = None
            user.is_active = True
            user.save()
            auth.login(request, user)
        return render(request, 'users/verification.html')
    except Exception as E:
        return HttpResponseRedirect(reverse('index'))
