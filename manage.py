import os

from flask.ext.script import Manager, Shell, Server, Command

from pgLP.app import create_app
from pgLP.settings import DevConfig, ProdConfig
from pgLP.public import EmailLead
from pgLP.extensions import db

if os.environ.get("PGLP_ENVIRONMENT") == 'prod':
    app = create_app(ProdConfig)
else:
    app = create_app(DevConfig)

manager = Manager(app)

def _makecontext():
    return {'app': app, 'db': db, 'EmailLead': EmailLead}

manager.add_command('shell', Shell(make_context=_makecontext))

@manager.command
def addLead(name, email, contact=True):
    newLead = EmailLead(name, email, contact)
    db.session.add(newLead)
    db.session.commit()
    print "User added"


if __name__ == "__main__":
    manager.run()
