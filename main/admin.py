from django.contrib import admin
from .models import Task
from .models import Calls
from .models import Lesson
from .models import User
from .models import Video
from .models import logup
from .models import update_up
from .models import photo_class
from .models import fizika
from .models import russian_language

admin.site.register(Task)
admin.site.register(Calls)
admin.site.register(Lesson)
admin.site.register(User)
admin.site.register(Video)
admin.site.register(logup)
admin.site.register(update_up)
admin.site.register(photo_class)
admin.site.register(fizika)
admin.site.register(russian_language)