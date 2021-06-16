from django.db import models


class BaseTextBlock(models.Model):
    class Meta:
        abstract = True

    text = models.CharField(max_length=1024)
    author = models.CharField(max_length=50, blank=True, default='unknown')
    rating = models.IntegerField(default=0, blank=True)

    def get_author(self):
        return f'{type(self).__name__} #{self.id}' if self.author is None else self.author

    def brief_info(self, max_length=120):
        if len(self.text) <= max_length:
            return self.text
        else:
            return self.text[:max_length] + '...'


class Post(BaseTextBlock):
    title = models.CharField(max_length=100)

    def get_next(self):
        try:
            return Post.objects.filter(pk__gte=self.id)[1].id
        except Post.DoesNotExist:
            return self.id
        except IndexError:
            return self.id

    def get_prev(self):
        try:
            return Post.objects.filter(pk__lte=self.id).reverse()[1].id
        except Post.DoesNotExist:
            return self.id
        except IndexError:
            return self.id

    def get_answers(self):
        return Message.objects.filter(root_post=self)

    def __str__(self):
        return self.title


class Message(BaseTextBlock):
    root_post = models.ForeignKey('Post', on_delete=models.CASCADE, null=True)
    root_message = models.OneToOneField('Message', related_name='+', blank=True, null=True, on_delete=models.CASCADE)
    answers = models.ManyToManyField('Message', related_name='+', blank=True)

    def get_depth(self):
        if self.root_message is None:
            return 0
        else:
            depth = 1 + self.root_message.get_depth()
            return depth if depth <= 5 else 5

    def __str__(self):
        return self.brief_info(30)
