from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms import validators
from wtforms.validators import DataRequired
from wtforms.fields.simple import PasswordField, SubmitField, TextAreaField


class electionForm(FlaskForm):
    president =SelectField('President',validators=[DataRequired()],choices=['','Mr. Nsima Akpan Edittu','Rev. Ekwere Udo Joshua'])
    vice_president=SelectField('Vice President',validators=[DataRequired()], choices=['','Mr. Akpapan Green Ufot','Mr. Inyang  Udoma'])
    secretary_general=SelectField('Secretary General',validators=[DataRequired()],choices=['','Mr. Ubong Akpan Essien','Barr. Ekong E. Umorok'])
    assistant_secretary = SelectField('Assistant Secretary',validators=[DataRequired()],choices=['','Mr. Ekwere Udo Nta'])
    treasurer = SelectField('Treasurer',validators=[DataRequired()],choices=['','Eldr. Obot Brown Udoete'])
    financial_secretary = SelectField('Financial Secretary',validators=[DataRequired()],choices=['','Mr. Emmanuel Samuel James'])
    publicity_secretary = SelectField('Publicity Secretary',validators=[DataRequired()],choices=['','Mr. John Fetus Obotowo','Eng. Samuel Ukoyen'])
    asst_publicity_secretary = SelectField('Asst. Publicity Secretary',validators=[DataRequired()],choices=['','Mr. Victor Efra Essien','Mr. Nsikan Friday Udoh','Hon. Emmanuel Ekwere'])
    provost= SelectField('Provost',validators=[DataRequired()],choices=['','Mr. Austin Bassey Lazarus'])
    asst_provost= SelectField('Asst. Provost',validators=[DataRequired()],choices=['','Mr. Ubong Udo Amos'])
    welfare_officer= SelectField('Welfare Officer',validators=[DataRequired()],choices=['','Hon. Ini Ebong Udose'])
    women_leader= SelectField('Women Leader',validators=[DataRequired()],choices=['','Ms. Glory','Mkapanam  Udom'])
    youth_leader= SelectField('Youth Leader',validators=[DataRequired()],choices=['','Mr. Stephen Okon Monday'])
    ex_officio= SelectField('Ex Officio',validators=[DataRequired()],choices=['','Pst. Idongesit Udofot Umoh'])
    auditors= SelectField('Auditors',validators=[DataRequired()],choices=['','Mr. John Dennis Urua'])
    legal_advisor= SelectField('Legal Advisor',validators=[DataRequired()],choices=['','Barr. Ime Sampson Essien'])
    
    submit = SubmitField('Submit All')