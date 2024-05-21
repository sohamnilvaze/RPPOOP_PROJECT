
from datetime import datetime
from tut3 import db , login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20),unique=True, nullable=False)
    email= db.Column(db.String(120),unique=True, nullable=False)
    image_file = db.Column(db.String(20) , nullable=False , default = 'default.jpg')
    password = db.Column(db.String(60), nullable=False )

    def __repr__(self):
        return f"User('{self.username}' , '{self.email}' , '{self.image_file}' )"
        
        
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime , nullable = False, default=datetime.utcnow )

    def __repr__(self):
        return f"Post('{self.title}' , '{self.date_posted}' )"

class TrainsList(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    trainno=db.Column(db.String(10),nullable=False)
    trainname=db.Column(db.String(100),nullable=False)
    startstation=db.Column(db.String(100),nullable=False)
    endstation=db.Column(db.String(100),nullable=False)
    days=db.Column(db.String(100),nullable=False)
    departuretime=db.Column(db.String(10),nullable=False)
    arrivaltime=db.Column(db.String(10),nullable=False)
    coaches=db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return f"TrainsList('{self.trainno}','{self.trainname}','{self.startstation}','{self.endstation}','{self.days}','{self.departuretime}','{self.arrivaltime}','{self.coaches}')"
    

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20), nullable=False)
    email= db.Column(db.String(120), nullable=False)
    seatno=db.Column(db.Integer , nullable = False)
    startstation = db.Column(db.String(120), nullable=False)
    endstation = db.Column(db.String(120) , nullable=False)
    coachname = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Booking('{self.username}','{self.email}','{self.seatno}','{self.startstation}','{self.endstation}',{self.coachname}' )"
    
class SeatBookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20), nullable=False)
    email= db.Column(db.String(120), nullable=False)
    seatno=db.Column(db.Integer , nullable = False)
    startstation = db.Column(db.String(120), nullable=False)
    endstation = db.Column(db.String(120) , nullable=False)
    coachname = db.Column(db.String(20), nullable=False)


    def __repr__(self):
        return f"SeatBookings('{self.username}','{self.email}','{self.seatno}','{self.startstation}','{self.endstation}','{self.coachname}' )"

class TicketBookings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(20), nullable=False)
    email= db.Column(db.String(120), nullable=False)
    trainname=db.Column(db.String(120), nullable=False)
    trainnumber=db.Column(db.String(120),nullable=False)
    dateoftravel=db.Column(db.String(120), nullable=False)
    seatno=db.Column(db.Integer , nullable = False)
    startstation = db.Column(db.String(120), nullable=False)
    endstation = db.Column(db.String(120) , nullable=False)
    coachname = db.Column(db.String(20), nullable=False)


    def __repr__(self):
        return f"TicketBookings('{self.username}','{self.email}','{self.trainname}','{self.trainnumber}','{self.dateoftravel}','{self.seatno}','{self.startstation}','{self.endstation}','{self.coachname}' )"

def init_db():
    db.create_all

if __name__ == '__main__':
    init_db()
