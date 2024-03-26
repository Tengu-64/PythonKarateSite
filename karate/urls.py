from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),# главная страница
    path('belt/', belt, name='belt'),# система поясов
    path('exam/', exam, name='exam'),# нормативы экзаменов (ссылки)
    path('exam/<int:exam_id>', concrete_exam, name='concrete_exam'),
    path('power/', power, name='power'),# проверка уровня (форма)
    path('dictionary/', dictionary, name='dictionary'),# словарь
]

