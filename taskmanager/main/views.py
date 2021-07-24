from django.shortcuts import render
from .models import Task
from .models import photo_class
from .models import Calls
from .models import Lesson
from .models import User
from .models import Video
from .models import logup
from .models import update_up
from .models import russian_language
from .models import fizika


def physics(request):
    tasks = fizika.objects.all()
    return render(request, 'main/Physics.html', {'title': 'Логин', 'tasks': tasks})

def login(request):
    tasks = logup.objects.all()
    return render(request, 'main/login.html', {'title': 'Логин', 'tasks': tasks})

def helper_views(request):
    return render(request, 'main/help_as.html')

def helper(request):
    return render(request, 'main/helper_main.html')

def main_page(request):
    tasks = Task.objects.all()
    return render(request, 'main/main_page.html', {'title': 'Главная страница сайта', 'tasks': tasks})

def life_class(request):
    tasks = photo_class.objects.all()
    return render(request, 'main/life_class.html', {'title': 'Новости класса', 'tasks': tasks})

def calls(request):
    tasks = Calls.objects.all()
    return render(request, 'main/calls.html', {'title': 'Расписание звонков', 'tasks': tasks})

def lesson(request):
    tasks = Lesson.objects.all()
    return render(request, 'main/lesson.html', {'title': 'Расписание звонков', 'tasks': tasks})

def user_class_list(request):
    tasks = User.objects.all()
    return render(request, 'main/user_class_list.html', {'title': 'Расписание звонков', 'tasks': tasks})

def mathematics(request):
    tasks = Video.objects.all()
    return render (request, 'main/mathematics.html', {'title': 'Хелпа матеша', 'tasks': tasks})

def update(request):
    tasks = update_up.objects.all()
    return render (request, 'main/logup.html', {'title': 'Обновления', 'tasks': tasks})

def russian(request):
    tasks = russian_language.objects.all()
    return render(request, 'main/Russian_language.html', {'title': 'Обновления', 'tasks': tasks})


