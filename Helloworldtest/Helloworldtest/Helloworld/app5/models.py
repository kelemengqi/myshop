from django.db import models


class UserBaseInfo(models.Model):
    id = models.AutoField(verbose_name='编号', primary_key=True)
    username = models.CharField(verbose_name='用户名称', max_length=30)
    password = models.CharField(verbose_name='密码', max_length=10)
    age = models.IntegerField(verbose_name="年龄", default=1)
    mobile = models.CharField(verbose_name="手机号码", max_length=11)
    status = models.CharField(verbose_name="状态", max_length=1)
    createdate = models.DateTimeField(verbose_name='创建日期', db_column='createDate', auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        verbose_name = "人员基本信息"
        db_table = 'UserBaseInfo5'

# Create your models here.
