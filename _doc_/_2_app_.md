### 创建APP流程
- add _app_\
- 使用PyCharm中manage.py工具
- startapp _app_._library_
- mv _library_\ -> _app_\
- 修改 _library_\apps.py
    - ```
    from django.apps import AppConfig
    class LibraryConfig(AppConfig):
        name = '_app_._library_'
        verbose_name = '图书馆'
        verbose_name_plural = verbose_name
    ```
- 修改 _library_\__init__.py
    - ```
    default_app_config = "_app_._library_.apps.LibraryConfig"
    ```
- 修改 _django_\setting.py

- makemigrations
- migrate