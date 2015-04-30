
__author__ = 'Apple'

from app.models import Todo
from flask_script import Manager, Server
from app import app

manager = Manager(app)

manager.add_command("runserver",
         Server(host='127.0.0.1',port=27017, use_debugger=True))
if __name__ == '__main__':
    manager.run()


@manager.command
def save_todo():
    todo = Todo(content="my first todo")
    todo.save()


