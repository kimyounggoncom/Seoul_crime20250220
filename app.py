from flask import Flask, render_template, request

from com.kimyounggoncom.models.police_controller import PoliceController

app = Flask(__name__)

@app.route('/')
def index():
   controller = PoliceController()
   controller.modeling('cctv_in_seoul.csv', 'crime_in_seoul.csv', 'pop_in_seoul.xls')
   return render_template("index.html")

@app.route('/police')
def police():
   return render_template("police.html")





if __name__ == '__main__':
     
   app.run('0.0.0.0',port=5000,debug=True)

   app.config['TEMPLATES_AUTO_RELOAD'] = True