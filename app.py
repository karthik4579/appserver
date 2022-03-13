from flask import Flask
from flask import request
from encrypt import ncrypt, dcrypt
app = Flask(__name__)


@app.route('/encrypt', methods=["POST"])
def Encrypt():
    value0 = str(request.form['activity'])
    if(value0 == "register"):
        valuer1 = str(request.form['password'])
        valuer2 = str(request.form['nfcpassword'])
        a = ncrypt(valuer1, valuer2)
        return a

    elif(value0 == "nfcreset"):
        valuen1 = str(request.form['newnfcpassword'])
        b = ncrypt(valuen1)
        return b

    elif(value0 == "userpassreset"):
        valueu1 = str(request.form['newuserpassword'])
        c = ncrypt(valueu1)
        return c



@app.route('/dcrypt', methods=["POST"])
#This is for login so this will take password decrypt it and return it
def Decrypt(): 
        valuel1 = str(request.form['password'])
        d = dcrypt(valuel1)
        return d