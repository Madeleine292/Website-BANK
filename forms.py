from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators, ValidationError, DateField, EmailField
from wtforms.fields import IntegerField, SelectField, DecimalField
from datetime import datetime
from model import Account



class NewCustomerForm(FlaskForm):
    GivenName = StringField('name', validators=[validators.DataRequired(), validators.Length(max=50)])
    Surname = StringField('name', validators=[validators.DataRequired(), validators.Length(max=50)])
    City = StringField('city', validators=[validators.DataRequired(), validators.Length(max=50)])
    Streetaddress = StringField('streetaddress', validators=[validators.DataRequired(), validators.Length(max=50)])
    Zipcode = IntegerField('zipcode', validators=[validators.DataRequired()])
    Country = StringField('streetaddress', validators=[validators.DataRequired()])
    NationalId = StringField('NationalId', validators=[validators.DataRequired()])
    CountryCode = SelectField('countryCode',choices=[('46','+46'),('41','+41'),('42','+42')])
    Birthday = DateField('Birthday', validators=[validators.DataRequired()])
    EmailAddress = EmailField('emailaddress', validators=[validators.DataRequired()])
    Telephone = StringField('Telephone', validators=[validators.DataRequired()])

class IdCustomerForm(FlaskForm):
    Id = IntegerField('Id', validators=[validators.DataRequired()])
    NationalId = StringField('NationalId', validators=[validators.DataRequired()])


class TransactionForm(FlaskForm):
    Amount = DecimalField('Amount', validators=[validators.DataRequired(), validators.NumberRange(min=1,max=5000)])

class TransferForm(FlaskForm):
    Amount = DecimalField('Amount', validators=[validators.DataRequired(), validators.NumberRange(min=1,max=5000)])
    Id = IntegerField('Id', validators=[validators.DataRequired()])
    
# class WithdrawForm(FlaskForm):
#     #todo icke negativt belopp
#     amount = IntegerField('amount', validators=[validators.DataRequired(), validators.NumberRange(min=1,max=1000000)])

