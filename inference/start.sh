#!/bin/bash
# 从第一行到最后一行分别表示：
# 1. 生成数据库可执行文件，
# 2. 根据数据库可执行文件来修改数据库
# 3. 使用 gunicorn 作为 wsgi  
python manage.py makemigrations&&
python manage.py migrate&&
gunicorn modayu.wsgi:application -c gunicorn.ini.py