from flask_script import Manager
from Map import app
from Map import db
from Map.user.models import User
from Map.event.models import Event


manager = Manager(app)


@manager.command
def db_create():
    try:
        db.create_all()
        print('you had create db')
    except:
        print('error!')

    user = User()
    args = {}
    args['phone'] = '12345678910'
    args['password'] = '123456'
    
    event = Event()



    try:
        user.save(args)
    except:
        print(args['username'], ' load error!')


    print('load over!')


if __name__ == '__main__':
    manager.run()
