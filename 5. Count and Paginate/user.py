# ========== User Model ==========
# import all package
import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase('python-peewee', user='root', password='root')

class User(peewee.Model) :
	name = peewee.CharField()
	email = peewee.CharField()
	# how to create a default value
	# fieldName = peewee.CharField(default='the default value')

	class Meta :
		database = db
	

db.connect()
db.create_tables([User], safe=True)

print('========== How to Get the total data ==========')
print(User.select().count())

print('========== How to Handle Pagination ==========')
# User.select().paginate(page, total data per page)
print(User.select().paginate(2, 5).count())