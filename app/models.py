from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash



#! User names cannot contain '-', its used in js for cutting out id
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    gender = db.Column(db.String(16), nullable=False, default="")

    # Boolean, will impact user rendering
    online = db.Column(db.Boolean, nullable=False, default=True)
    
    # For example: 'polish', 'photographer', 'engineer', 'bielsko'
    paramaters = db.Column(db.Text, nullable=False, default="")

    location = db.Column(db.String(128), nullable=False, default="")
    age = db.Column(db.Integer, nullable=False, default="")

    # Descriptions
    work_related = db.Column(db.Text, nullable=False, default="")
    about_me = db.Column(db.Text, nullable=False, default="")
    hobbies = db.Column(db.Text, nullable=False, default="")

    profile_image = db.Column(db.String(256), nullable=False, default="https://avatarfiles.alphacoders.com/101/101741.jpg") 
    background_image = db.Column(db.String(256), nullable=False, default="") #! Delete
    
    # Social Media Links
    facebook = db.Column(db.String(128), nullable=False, default="")
    spotify = db.Column(db.String(128), nullable=False, default="")
    youtube = db.Column(db.String(128), nullable=False, default="")
    twitter = db.Column(db.String(128), nullable=False, default="")


    def check_username(self, username):
        if '-' in username:
            return False
        return True


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def __repr__(self):
        return f'User: {self.username}'


    def checkFacebook(self, link):
        if "https://www.facebook.com/" in link:
            return True
        return False


    def checkSpotify(self, link):
        if "https://open.spotify.com/" in link:
            return True
        return False


    def checkYoutube(self, link):
        if "https://www.youtube.com/channel/" in link:
            return True
        return False


    def checkTwitter(self, link):
        if "https://twitter.com/" in link:
            return True
        return False


    def checkImg(link):
        return link[(len(link) - 4):] in ['.jpg', '.png']


    # TODO
    #* Functions checking db.Text (scanning for cuss words etc.)
    #! Functions hashing the password

    #! TODO 
    #* Run test cases for creating fake users, deleting fake users
    #* Build up the search query/filter while having those users


# Flask-Login Necessity
@login.user_loader
def load_user(id):
    return User.query.get(int(id))