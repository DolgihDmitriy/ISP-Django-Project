from asgiref.sync import sync_to_async
from django.urls import reverse_lazy


@sync_to_async
def get_all_access(self):
    return reverse_lazy('tasks')
