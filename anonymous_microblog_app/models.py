from django import forms
from django.db import models

class Post(models.Model):

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    text = models.TextField(verbose_name='Текст')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Время')

    def __str__(self):
        return (str(self.timestamp) if self.timestamp else '') + (self.text[:30] if self.text else '')


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('text',)