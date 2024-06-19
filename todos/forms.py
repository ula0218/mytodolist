from django.db import models


class ToDoList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def formatted_created_at(self):
        return self.created_at.strftime("%Y/%m/%d %H:%M")