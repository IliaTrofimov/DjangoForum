import django.db.models
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=1024)
    author = models.CharField(max_length=50, blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True)

    def get_answers(self):
        return Message.objects.filter(root_post=self)

    def brief_info(self):
        if len(self.text) <= 60:
            return self.text
        else:
            return self.text[:60] + '...'

    def vote_up(self):
        self.rating += 1

    def vote_down(self):
        self.rating += 1

    def __str__(self):
        return self.title


class Message(models.Model):
    text = models.CharField(max_length=256)
    root_post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    root_message = models.OneToOneField('Message', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    answers = models.ManyToManyField('Message', related_name='+', blank=True)
    rating = models.IntegerField(default=0, blank=True)
    author = models.CharField(max_length=50, blank=True, null=True)

    def get_depth(self):
        if self.root_message is None:
            return 0
        else:
            depth = 1 + self.root_message.get_depth()
            return depth if depth <= 5 else 5

    def vote_up(self):
        self.rating += 1

    def vote_down(self):
        self.rating += 1

    def __str__(self):
        if len(self.text) <= 30:
            return self.text
        else:
            return self.text[:30] + '...'
