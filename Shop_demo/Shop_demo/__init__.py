import pymysql
pymysql.install_as_MySQLdb()
"""在启动我们的Django项目前，我们需要激活我们的mysql。
然后，启动项目，会报错：no module named MySQLdb 。
这是因为django默认你导入的驱动是MySQLdb，
可是MySQLdb 对于py3有很大问题，所以我们需要的驱动是PyMySQL 
所以，我们只需要找到项目名（project）文件下的__init__（Django/Django/__init__.py），
在里面写入"""