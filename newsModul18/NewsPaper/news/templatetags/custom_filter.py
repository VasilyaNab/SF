import re
from django import template

register = template.Library()

@register.filter
def censor(text):
    if not isinstance(text, str):
        return text  # Возвращаем текст без изменений, если это не строка
    bad = ['помидорка', 'помидорки', 'ягодка']  # Замените на ваши нежелательные слова
    for word in bad:
        text = re.sub(r'(?i){}'.format(re.escape(word)), '*' * len(word), text)
    return text