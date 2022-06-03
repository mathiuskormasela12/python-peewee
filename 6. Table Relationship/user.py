# ============== Table Relationship ==============
# import all packages
import peewee
from playhouse.mysql_ext import MySQLConnectorDatabase

db = MySQLConnectorDatabase('peewee-relationship', user = 'root', password = 'root')

class BaseModel(peewee.Model) :
	class Meta :
		database = db
	

class User(BaseModel) :
	name = peewee.CharField()
	email = peewee.CharField()

class Task(BaseModel) :
	uid = peewee.ForeignKeyField(User, backref='tasks')
	task_name = peewee.CharField()

db.connect()
db.create_tables([User, Task])

users = (
	{
		'name': 'yerin',
		'email': 'yerin@sublime.ko.kr'
	}
)

tasks = (
	{
		'uid': 1,
		'task_name': 'Release Aria song'
	}
)

# User.insert_many(users).execute()
# Task.insert_many(tasks).execute()

print('========== Select Data Using join method ==========')
userTasks = User.select(Task.task_name).join(Task).dicts()
print(list(userTasks))

print('========== Select Data Using backref keyword ==========')
data = User.get()
print(list(data.tasks.dicts()))