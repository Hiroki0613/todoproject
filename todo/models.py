from django.db import models

# タプル型で表示。左はコードに書き込まれるもの、右側はweb上で表示されるもの
PRIORITY = (('danger', 'high'), ('info', 'normal'), ('success', 'low'))


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        # 上のPRIORITYで記載したものがchoicesに表示される
        choices=PRIORITY
    )
    # 日付を表示するもの
    duedate = models.DateField()

    # メイン項目をString型で表示してくれるもの
    def __str__(self):
        return self.title
