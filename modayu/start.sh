#!/bin/bash
# 从第一行到最后一行分别表示：
# 1. 收集静态文件到根目录，
# 2. 生成数据库可执行文件，
# 3. 根据数据库可执行文件来修改数据库
python manage.py makemigrations&&
python manage.py migrate&&
python manage.py runsever 0.0.0.0:8090