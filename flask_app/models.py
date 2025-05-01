from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


# TODO: implement
@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

# TODO: implement fields
class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True, min_length=1, max_length=40)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True)
    profile_pic = db.ImageField()

    # Returns unique string identifying our object
    def get_id(self):
        # TODO: implement
        return self.username


# TODO: implement fields
class watchedStock(db.Document):
    watcher = db.ReferenceField(User, required=True)
    date = db.StringField(required=True)
    name = db.StringField(required=True)
    symbol = db.StringField(required=True)
    high = db.FloatField(required=True)
    low = db.FloatField(required=True)
    image = db.StringField()
    #Uncomment when other fields are ready for review pictures