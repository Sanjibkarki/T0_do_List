from django.shortcuts import render, HttpResponseRedirect, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from .models import register, event
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.views.decorators.cache import cache_control
import calendar
from datetime import date

def cld():
    today = date.today()
    text_cal = calendar.HTMLCalendar(firstweekday=-1)
    year = today.year
    return text_cal.formatyear(year, 4)
class SignUpView(View):
    @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True))
    def get(self, request):
        return render(request, "Activity/signup.html")

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        if pass1 != pass2:
            return HttpResponse("<p>Sorry, the password doesn't match</p><a href='signup'>Try again</a>")
        else:
            reg = User.objects.create_user(username=email, first_name=fname, last_name=lname, email=email, password=pass1)
            reg.save()
            auth_user = authenticate(request, username=email, password=pass1)
            login(request, auth_user)
            return redirect('homepage')
        
class IndexView(LoginRequiredMixin,View):
    @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True))
    
    def get(self, request):
        return render(request, "index.html", {"year": cld()})
    
class LoginView(View):
    @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True))
    def get(self, request):
        return render(request, 'Activity/login.html')

    def post(self, request):
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        user = authenticate(request, username=email, password=pass1)

        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, "Activity/login.html")

class PostView(LoginRequiredMixin,View):
    def post(self, request):
        day = request.POST.get('Day')
        month = request.POST.get('Month')
        activity = request.POST.get('activity')
        add = event(user=request.user, day=day, month=month, activity=activity)
        add.save()
        return HttpResponseRedirect(reverse('homepage'))

    def get(self, request):
        return render(request, 'task.html')

class LogoutView(View):
    @method_decorator(cache_control(no_cache=True, must_revalidate=True, no_store=True))
    def get(self, request):
        request.session.clear() 
        logout(request)
        return redirect('log_in')


class DetailView(LoginRequiredMixin,View):
    def get(self, request):
        try:
            even = event.objects.filter(user=request.user).values()

            return render(request, 'detail.html', {'data': even})
        except event.DoesNotExist:
            return render(request, 'detail.html')

class DeletesView(LoginRequiredMixin,View):
    def get(self, request, id):
        data = event.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect(reverse('details'))
