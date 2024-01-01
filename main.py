from flask import Flask, render_template,jsonify
import pandas as pd

print("Hello")
app = Flask(__name__)

df =pd.read_csv("dictionary.csv")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<word>/')
def api(word):
    print("Hi")
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    result_dictionary = {'word':word,'definition':definition}
    return result_dictionary

if __name__ == '__main__':
    app.run(debug=True,port=5001)       #Give different port name as another app has port 5000. If apps using same ports are run at the same time error occurs due to clash
