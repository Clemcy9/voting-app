from flask import render_template, url_for,flash,redirect,request
from voting_app.forms import electionForm
from voting_app import app,db
from voting_app.models import Election, User, Poll

postions=['President','Vice President','Secretary General','Assistant Secretary','Treasurer','Financial Secretary','Publicity Secretary','Asst. Publicity Secretary','Provost','Asst. Provost','Welfare Officer','Women Leader','Youth Leader','Ex Officio','Auditors','Legal Advisor']

villages =['Essien Etuk','Abiaran','Obio Akama','Umeneke 1','Umeneke 2','Owok Abasi Etehe']



@app.route('/',methods=['GET','POST'])
def home():

    forms2 = electionForm()
    elec = Election.query.all()
    elec2 =Election
    user = User.query.all()
    poll = Poll

    electdict = {
        'President' : forms2.president,
        'Vice President' : forms2.vice_president,
        'Secretary General': forms2.secretary_general,
        'Assistant Secretary': forms2.assistant_secretary,
        'Treasurer' : forms2.treasurer,
        'Financial Secretary' : forms2.financial_secretary,
        'Publicity Secretary' : forms2.publicity_secretary,
        'Asst. Publicity Secretary' : forms2.asst_publicity_secretary,
        'Provost' : forms2.provost,
        'Asst. Provost' : forms2.asst_provost,
        'Welfare Officer' : forms2.welfare_officer,
        'Women Leader' : forms2.women_leader,
        'Youth Leader' : forms2.youth_leader,
        'Ex Officio' : forms2.ex_officio,
        'Auditors' : forms2.auditors,
        'Legal Advisor' : forms2.legal_advisor,
        'submit' : forms2.submit,
        'validate' : forms2.validate_on_submit()
    }

    

    if electdict['validate']:
        print(forms2.president.data)
        for x in postions:
            pool = Poll(who_to_vote= forms2[x.lower().replace('.','').replace(' ','_')].data,)
            db.session.add(pool)
            db.session.commit()
            print(forms2[x.lower().replace('.','').replace(' ','_')].data)
        return redirect(url_for('res'))

    return render_template('vote.html',title='vote',db=db,forms2=forms2,forms=postions, elec = elec, user =user, poll = poll, elec2=elec2, formdict= electdict)

@app.route('/result')
def res():
    elec2 =Election
    poll = Poll
    return render_template('vote copy.html',title ='Result', db=db,forms=postions,poll=poll,elec2=elec2)