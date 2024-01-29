from django.db import models


class PlusContent(models.Model):
    content = models.TextField()
    content_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plus_content'


class PlusUserDetail(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    isactive = models.IntegerField(db_column='isActive', default=1)  # Field name made lowercase.
    content_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'plus_user_detail'

