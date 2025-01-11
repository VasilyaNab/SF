from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    ordering = '-created_at'  # Сортировка по дате публикации от более свежей к старой
    template_name = 'news.html'  # Шаблон для списка новостей
    context_object_name = 'news'  # Имя контекста для списка новостей

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # Текущее время
        context['next_sale'] = "Новости совсем скоро!"  # Дополнительное сообщение
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'new.html'  # Шаблон для детальной информации о новости
    context_object_name = 'new'  # Имя контекста для выбранной новости