# ============ Insert Data ============
# import all packages
import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase('python-peewee', user='root', password='root')

class User (peewee.Model) :
	name = peewee.CharField()
	email = peewee.CharField()

	class Meta :
		database = db

db.connect()
db.create_tables([User], safe=True)

# Insert A Row
# Option 1 => this method will return the id (auto increment)
# print(User.create(name='mathiusqwe', email='123'))
# Option 2 => it will return 1 if the data was created successfully
# user = User(name='eunha', email='eunha@viviz.ko.kr')
# print(user.save())

# Bulk Insert
# Option 1 => it will return the total data that is inserted successfully
# data = [
# 	{
# 		'name': 'sinb',
# 		'email': 'sinbi@viviz.ko.kr'
# 	},
# 	{
# 		'name': 'umji',
# 		'email': 'umji@viviz.ko.kr'
# 	},
# 	{
# 		'name': 'yerin',
# 		'email': 'yerin@gfriend.co.kr'
# 	}
# ]

# print(User.insert_many(data).execute())
# Option 2 => it will return the total data that is inserted successfully
fields = ['name', 'email']
values = [('yuju', 'yuju.konnect.ko.kr')]
print(User.insert_many(values, fields=fields).execute())