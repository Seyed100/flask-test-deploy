from flask import Flask, render_template , request

from forms import GetDataForm 


app = Flask(__name__)

app.secret_key = "ufsk;gj;sjlflihflslfblsjfe"

@app.route('/')
def OnIndex():
    return render_template('Home.html')

@app.route('/login')
def OnLogin():
    return render_template('Login.html')


@app.route('/getdata' , methods = ['GET' , 'POST'])
def GetData():
    form = GetDataForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            print ('Validate Form Successfully')
            pass
        else:
            print('Error in Form')
    return render_template('GetData.html' , form = form)

if __name__ == '__main__':
    app.run(debug = True)