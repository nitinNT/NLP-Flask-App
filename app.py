from flask import Flask, request, redirect, url_for, flash, jsonify,render_template
import pickle


app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def welcome():
    return render_template('index.html')

@app.route('/api/', methods=['GET','POST'])
def api():
    if request.method=='POST':
        data=request.form.get('check_text')
        if len(data)==0:
            message="Enter some text"
        else:
            sample=data.split(",")

            sample=tfidf.transform(sample).toarray()

            if clf.predict(sample)==1:
                message="Positive Comment"
            else:
                message="Negative Comment"
        return render_template('index.html',message=message)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    clf=pickle.load(open('classifier.pickle','rb'))
    tfidf=pickle.load(open('tfidfmodel.pickle','rb'))
    app.run(threaded=True, port=5000)