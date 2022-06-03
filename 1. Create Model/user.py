# ========== User Model ==========
# import all packages
import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

# need to run this code pip install mysql-connector-python

db = MySQLConnectorDatabase('python-peewee', user='root', password='root')

class User(peewee.Model) :
	name = peewee.CharField()
	email = peewee.CharField()

	class Meta :
		database = db
	

db.connect()
db.create_tables([User], safe=True)