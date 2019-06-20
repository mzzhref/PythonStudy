from django.db import models,transaction

# Create your models here.

class User(models.Model):
    """
    用户信息表
    """

    user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    user_guid = models.CharField(max_length=150, verbose_name='用户guid')
    user_name = models.CharField(
        max_length=100, blank=True, null=True, verbose_name='用户名')
    real_name = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='真实姓名')
    avatar = models.CharField(
        max_length=250, blank=True, null=True, verbose_name='头像')
    mobile = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='手机')
    balance = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='账户余额')
    available_balance = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='可用金额')
    frozen_balance = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='冻结金额')
    all_balance = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, null=True, verbose_name='累计金额')
    wx_open_id = models.CharField(max_length=150, verbose_name='微信OpenID')
    wx_union_id = models.CharField(
        max_length=150, blank=True, null=True, verbose_name='微信UnionID')
    create_date = models.FloatField(blank=True, null=True, verbose_name='创建时间')
    last_login_date = models.FloatField(
        blank=True, null=True, verbose_name='最后登录时间')
    ip_address = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='IP地址')
    gender = models.IntegerField(blank=True, null=True, verbose_name='性别')
    province = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='省份')
    city = models.CharField(
        max_length=50, blank=True, null=True, verbose_name='城市')
    session_key = models.CharField(
        max_length=150, blank=True, null=True, verbose_name='会话秘钥')
    is_notify = models.IntegerField(blank=True, null=True, verbose_name='是否开启打卡通知')

    @classmethod
    def update_user_balance(cls, user_id, amount):
        with transaction.atomic():
            user=(
                cls.objects
                .select_for_update()
                .get(user_id=user_id)
            )
            user.available_balance += amount
            user.balance = user.available_balance + user.frozen_balance
            if amount > 0:
                user.all_balance += amount
            user.save()
        return user

    class Meta:
        # managed = True # Django会自动根据模型类生成映射的数据库表，如果你不希望Django这么做，可以把managed的值设置为False
        ordering = ['-create_date']
        verbose_name = '用户'
        verbose_name_plural = '用户'


class Student(models.Model):
    s_id = models.CharField(primary_key=True, max_length=32, verbose_name='学生ID')
    s_name = models.CharField(max_length=20, verbose_name='学生姓名')
    s_age = models.IntegerField(verbose_name='学生年龄')
    s_sex = models.IntegerField(default=0, verbose_name='性别 0 男  1 女')
    s_class = models.IntegerField(verbose_name='班级')

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = verbose_name
