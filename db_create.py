from main import db
from models import BlogPost

# create the database and tables
db.create_all()


# insert
db.session.add(BlogPost("Good","I\'m good."))
db.session.add(BlogPost("Well","I\'m well."))



# commit changes
db.session.commit()
