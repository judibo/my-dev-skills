from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Skill
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class SkillCreate(CreateView):
    model = Skill
    fields = ['description', 'skill_level']
    success_url = '/skills'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class SkillUpdate(UpdateView):
    model = Skill
    fields = ['description', 'skill_level']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/skills/')

class SkillDelete(DeleteView):
  model = Skill
  success_url = '/skills'


# Create your views here.
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/skills')
                else:
                    print("The account has been disabled.")
                    return HttpResponseRedirect('/')
            else:
                print("The username and/or password is incorrect.")
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def skills_index(request):
    skills = Skill.objects.all()
    return render(request, 'skills/index.html', {'skills': skills})

def skills_detail(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    return render(request, 'skills/detail.html', {'skill': skill})

def about(request):
    return render(request, 'about.html')