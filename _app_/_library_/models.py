from datetime import datetime

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=30, verbose_name="图书名")
    create_date = models.DateTimeField(default=datetime.now, verbose_name="创建时间")
    update_date = models.DateTimeField(default=datetime.now, verbose_name="修改时间")

    class Meta:
        db_table = 'db_book'
        verbose_name = '图书'
        verbose_name_plural = verbose_name


class Point(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, verbose_name="图书")
    value = models.IntegerField()

    class Meta:
        db_table = 'db_point'
        verbose_name = '图书积分'
        verbose_name_plural = verbose_name


class Image(models.Model):
    name = models.CharField(max_length=300, verbose_name='图片名')
    url = models.URLField(max_length=300, verbose_name="图片地址")
    book = models.ManyToManyField(Book, verbose_name="图书")

    class Meta:
        db_table = 'db_image'
        verbose_name = '图书'
        verbose_name_plural = verbose_name


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name="作者名")
    books = models.ManyToManyField(Book, through='BookAuthor')

    class Meta:
        db_table = 'db_author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name


class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'db_book_author'
        verbose_name = '图书-作者'
        verbose_name_plural = verbose_name
