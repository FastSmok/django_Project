from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название задачи")
    completed = models.BooleanField(default=False, verbose_name="Выполнено")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")

    def __str__(self):
        return self.title
