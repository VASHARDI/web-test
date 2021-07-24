from django.db import models

class Task(models.Model):
    title = models.CharField('Название', max_length=10000)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

class Calls(models.Model):
    title = models.CharField('Название', max_length=10000)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField('Название', max_length=10000)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

class User(models.Model):
    title = models.CharField('Название', max_length=10000)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField('Название темы', max_length=10000)
    task0 = models.TextField('URL-video')
    task1 = models.TextField('URL доп.материалов')

    def __str__(self):
        return self.title

class logup(models.Model):
    title = models.CharField('Версия сайта', max_length=20)

    def __str__(self):
        return self.title

class update_up(models.Model):
    title = models.CharField('Версия сайта', max_length=20)
    task = models.TextField('Список изменений')

    def __str__(self):
        return self.title

class photo_class(models.Model):
    title = models.CharField('Имя сетки', max_length=20)
    task0 = models.TextField('URL фото')
    task1 = models.TextField('URL фото')
    task2 = models.TextField('URL фото')
    task3 = models.TextField('URL фото')
    task4 = models.TextField('URL фото')
    task5 = models.TextField('URL фото')
    task6 = models.TextField('URL фото')
    task7 = models.TextField('URL фото')
    task8 = models.TextField('URL фото')
    task9 = models.TextField('URL фото')

    def __str__(self):
        return self.title


class russian_language(models.Model):
    title = models.CharField('Название темы', max_length=1000)
    task0 = models.TextField('URL-video')
    task1 = models.TextField('URL доп. материалов')

    def __str__(self):
        return self.title

class fizika(models.Model):
    title = models.CharField('Название темы', max_length=1000)
    task0 = models.TextField('URL-video')
    task1 = models.TextField('URL доп. материалов')

    def __str__(self):
        return self.title