from django.contrib.auth.models import User
from django.db import models
from django_cron import CronJobBase, Schedule


class Post(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField(blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    author_name = models.CharField(max_length=255, blank=True)
    amount_of_upvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class PostUpvote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class UpvoteResetCronJob(CronJobBase):
    MINS = 24 * 60  # every 24 hours
    RETRY = 5
    schedule = Schedule(run_every_mins=MINS, retry_after_failure_mins=RETRY)

    code = "news.upvote_reset_cron_job"  # a unique code

    def do(self):
        Post.objects.update(amount_of_upvotes=0)
        PostUpvote.objects.all().delete()
