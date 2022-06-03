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

print('=============== Option 1 ===============')
# Option 1
# these one will return the value of id field
print(User.get(User.id == 1))
print(User.get(User.id == 1).id)
# this one will return the value of name field
print(User.get(User.id == 1).name)
# this one will return the value of email field
print(User.get(User.id == 3).email)

print('')
print('=============== Option 2 ===============')
# Option 2
# these one will return the value of id field
print(User.get_by_id(3))
print(User.get_by_id(3).id)
# this one will return the value of name field
print(User.get_by_id(4).name)

print('')
print('=============== Option 3 ===============')
# Option 3
# these one will return the value of id field
user = User[4]
print(user)
print(user.id)
# these one will return the value of name field
print(user.name)

print('')
print('=============== Option 4 ===============')
# Option 4
# .dict berfungsi untuk membuat format data nya jadi dictionary
query = User.select().dicts()
print(query[0]['name'])
qr = User.select()
print(qr[1].email)
print(list(query))

# Filter Data
print('')
print('=============== How To Filter the data ===============')
# show only data that has 'eunha' as name
data_with_eunha_as_name = User.select().where(User.name == 'eunha').dicts()
print(list(data_with_eunha_as_name))
# show only data that has 'eunha' or 'yerin' as name
data_with_eunha_or_mathius_as_name = User.select().where(User.name == 'eunha' | User.name == 'yerin').dicts()
print(list(data_with_eunha_or_mathius_as_name))
# show only data that has 'eunha' as name and 3 as id
data_with_eunha_as_name_and_3_as_id = User.select().where(User.name == 'eunha', User.id == 3).dicts()
print('data that has \'eunha\' as name and 3 as id',list( data_with_eunha_as_name_and_3_as_id))
# show only data that has 'yerin' as name
data_contains = User.select().where(User.name.contains('yerin')).dicts()
print(list(data_contains))

# Sorting Data
print('')
print('=============== How To Sorting the data ===============')
ascData = User.select().order_by(User.id.asc()).dicts()
descData = User.select().order_by(User.id.desc()).dicts()
print('These are sorted', list(descData))