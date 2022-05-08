from django.shortcuts import render

# Create your views here.
def get_permissions(self):
    # Если в GET-запросе требуется получить информацию об объекте
    if self.action == 'retrieve':
        # Вернем обновленный перечень используемых пермишенов
        return (ReadOnly(),)
    # Для остальных ситуаций оставим текущий перечень пермишенов без изменений
    return super().get_permissions()