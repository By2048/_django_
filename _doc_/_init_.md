
### 环境初始化
- `install python-3.8.8-amd64.exe -> D:\python\3.8.8\`
- `D:\python\3.8.8\python.exe -m pip install --upgrade pip`
- `D:\python\3.8.8\Scripts\pip.exe install virtualenv`
- `cd D:\Python\`
- `D:\Python\3.8.8\Scripts\virtualenv.exe _django_ --python=D:\Python\3.8.8\python.exe`

### 项目初始化
- `cd D:\Python\_django_\`
- `.\Scripts\activate.ps1`
- `pip install django`
- `cd E:\Project\`
- `django-admin startproject _django_`

### Git初始化
- add `.gitignore`
  - ```
    .idea
    .vscode
    desktop.ini
    __pycache__/
    *.py[cod]
    ```
- `git init`
- `git commit -m "init"`
- `git branch -M main`
- `git remote add origin https://github.com/By2048/_django_.git`
- `git push -u origin main`

### 项目完善
- add `_doc_/`
- add `requirements_dev.txt`
- add `README.md`
- `pip freeze > requirements.txt`
