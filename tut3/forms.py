from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from flask_login import current_user
from wtforms import StringField , PasswordField , SubmitField , BooleanField , IntegerField , SelectField , DateField
from wtforms.validators import DataRequired , Length , Email , EqualTo , ValidationError ,NumberRange
from tut3.models import User, Booking , SeatBookings , TicketBookings ,TrainsList
from datetime import datetime
'''
STATION_CHOICES = [ ('Pune Junction','Pune Junction'),
    ('Daund Junction', 'Daund Junction'),
    ('Ahmadnagar', 'Ahmadnagar'),
    ('Kopargaon', 'Kopargaon'),
    ('Manmad Junction', 'Manmad Junction'),
    ('Bhusaval Junction', 'Bhusaval Junction'),
    ('Shegaon', 'Shegaon'),
    ('Akola Junction', 'Akola Junction'),
    ('Badnera Junction', 'Badnera Junction'),
    ('Dhamangaon', 'Dhamangaon'),
    ('Pulgaon Junction', 'Pulgaon Junction'),
    ('Wardha Junction', 'Wardha Junction'),
    ('Hinghat Junction', 'Hinghat Junction'),
    ('Warora', 'Warora'),
    ('Bhandak', 'Bhandak'),
    ('Chandrapur', 'Chandrapur'),
    ('Balharshah', 'Balharshah'),
    ('Ramagundam', 'Ramagundam'),
    ('Peddapalli', 'Peddapalli'),
    ('Kazipet Junction', 'Kazipet Junction')
]
'''
STATION_CHOICES = [('CSMT Junction','CSMT Junction'),('Pune Junction','Pune Junction')]
COACHES= [ ('DL1','DL1'),('DL2','DL2'),('S1','S1'),('S2','S2'),('S3','S3'),('S4','S4'),('S5','S5'),('S6','S6'),('S7','S7'),('S8','S8'),('S9','S9'),('S10','S10'),('S11','S11'),('B1','B1'),('B2','B2'),('B3','B3'),('B4','B4'),('B5','B5'),('B6','B6'),('A1','A1')]


class regform(FlaskForm):
	username = StringField('Username',validators=[DataRequired(), Length(min=8, max=20)])
	email=StringField('Email', validators=[DataRequired(), Email() ])
	password=PasswordField('Password',validators=[DataRequired(), Length(min=8)])
	confirm_password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	
	submit= SubmitField('Sign Up')
	
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is already been taken.Please try some other username')
	
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is already been taken.Please try some other email')


class loginform(FlaskForm):
	email=StringField('Email', validators=[DataRequired(), Email() ])
	password=PasswordField('Password',validators=[DataRequired(), Length(min=8)])
	remember=BooleanField('Remember Me')
	
	submit= SubmitField('Login')



class updateaccform(FlaskForm):
	username = StringField('Username',validators=[DataRequired(), Length(min=8, max=20)])
	email=StringField('Email', validators=[DataRequired(), Email() ])
	picture =  FileField('Update Profile Picture',validators=[FileAllowed(['jpg','png'])])
	
	submit= SubmitField('Update')
	
	def validate_username(self, username):
		if username.data!=current_user.username :
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('That username is already been taken.Please try some other username')
	
	def validate_email(self, email):
		if email.data!=current_user.email :
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('That email is already been taken.Please try some other email')
			

class bookform(FlaskForm):
	username= StringField('Username',validators=[DataRequired()])
	email=StringField('Email', validators=[DataRequired(), Email() ])
	trainname=SelectField('TrainName',validators=[DataRequired()])
	trainnumber=StringField('TrainNumber',validators=[DataRequired()])
	dateoftravel=StringField('DateofTravel',validators=[DataRequired()])
	#dateoftravel=DateField('Date of Travel',format='%d/%m/%Y',validators=[DataRequired()])
	seatno= IntegerField('Seatno',validators=[ DataRequired() , NumberRange( min=0, max=75)])
	#startstation = StringField('Startstation' , validators=[DataRequired()])
	startstation = SelectField('Startstation', choices=STATION_CHOICES, validators=[DataRequired()])
	endstation = SelectField('Endstation', choices=STATION_CHOICES, validators=[DataRequired()])
	#endstation = StringField('Endstation',validators=[DataRequired()])
	#coachname = StringField('Coachname',validators=[DataRequired()])
	coachname = SelectField('Coachname', choices= COACHES, validators=[DataRequired()])
	'''
	if (startstation.data==endstation.data):
		raise ValidationError('Please enter proper start and end stations. They should not be same')
	
	def __init__(self, *args, **kwargs):
    	super(bookform, self).__init__(*args, **kwargs)
        self.train_name.choices = [(train.trainname, train.trainname) for train in TrainsList.query.all()]
	'''
	def __init__(self, *args, **kwargs):
		super(bookform,self).__init__(*args,**kwargs)
		self.trainname.choices= [(train.trainname,train.trainname) for train in TrainsList.query.all()]
	'''
	def __init__(self,*args,**kwargs):
		super(bookform,self).__init__(*args,**kwargs)
		self.trainnumber.choices=[(train.trainno,train.trainno) for train in TrainsList.query.all()]
	'''
	submit=SubmitField('Book')
	'''
	def validate_dateoftravel(self,dateoftravel):
		if dateoftravel.data and dateoftravel.data < datetime.now().date():
			raise ValidationError('Please input a valid date!')
	'''


class deletebookingform(FlaskForm):
	username= StringField('Username',validators=[DataRequired()])
	email=StringField('Email', validators=[DataRequired(), Email() ])
	trainname=StringField('TrainName',validators=[DataRequired()])
	trainnumber=StringField('TrainNumber',validators=[DataRequired()])
	dateoftravel=StringField('DateofTravel',validators=[DataRequired()])
	seatno= IntegerField('Seatno',validators=[ DataRequired() , NumberRange( min=0, max=75)])
	coachname = SelectField('Coachname', choices= COACHES, validators=[DataRequired()])

	submit=SubmitField('Delete Seat Booking')

class addtrain(FlaskForm):
	trainno=StringField('Train No',validators=[DataRequired()])
	trainname=StringField('Train Name',validators=[DataRequired()])
	startstation=StringField('Start Station',validators=[DataRequired()])
	endstation=StringField('End Station',validators=[DataRequired()])
	days=StringField('Days',validators=[DataRequired()])
	departuretime=StringField('Departure Time',validators=[DataRequired()])
	arrivaltime=StringField('Arrival Time',validators=[DataRequired()])
	coaches=StringField('Coaches Available',validators=[DataRequired()])

	submit=SubmitField('Add Train')

class removetrain(FlaskForm):
	trainno=StringField('Train No',validators=[DataRequired()])
	trainname=StringField('Train Name',validators=[DataRequired()])

	submit=SubmitField('Remove Train')
	


	



	
	

	
	
	
	
	
	
