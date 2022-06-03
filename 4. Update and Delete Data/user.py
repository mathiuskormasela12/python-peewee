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

print('========== How To Update the Data ==========')
print('A. The first way')
data = User.select().where(User.id == 3).get()
data.name = 'Sowon'
data.email = 'sowon@gfriend.ko.kr'
data.save()

print('B. The second way')
User.update(name='matt').where(User.id == 5).execute()

print('========== How To Delete the Data ==========')
print('A. The first way')
# theData = User.get(User.name == 'matt')
# theData.delete_instance()
print('B The second way')
User.delete().where(User.id == 8).execute()