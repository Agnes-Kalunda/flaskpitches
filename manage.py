from app import create_app, db
from flask_script import Manager, Server	from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand	from flask_migrate import Migrate, MigrateCommand
app = create_app('development')	app = create_app('development')
manager = Manager(app)	manager = Manager(app)
manager.add_command('server', Server)	manager.add_command('server', Server)
migrate Migrate(app, db)	migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)	manager.add_command('db', MigrateCommand)


@manager.shell	@manager.shell
def make_shell_context():	def make_shell_context():
    return dict(app=app)	    return dict(app=app, db=db)




if __name__ == "__main__":
    manager.run()
