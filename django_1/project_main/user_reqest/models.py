from django.db import models


class User_request(models.Model):
    user_name = models.CharField('name', max_length=50)
    user_conact = models.CharField('contact', max_length=50)
    text_1 = models.TextField('text')
    pub_time = models.IntegerField('time')
    pub_date = models.IntegerField('date')

    def __str__(self):
        return self.user_name
    
    class Meta:
        verbose_name = 'Запросы'
        verbose_name_plural = 'Запрос'


# class Task(models.Model):
#     title = models.CharField('Имя пользователя', max_length=50)
#     text = models.TextField('Описание проблемы')
   
#     # pub_date = models.DateTimeField('date')

#     def __str__(self):
#         return self.title

# class Aricle(models.Model):
#     title_1 = models.CharField('name', max_length=50)
#     text_1 = models.TextField('text')
#     pub_date = models.TimeField('date')

#     def __str__(self):
#         return self.title_1


