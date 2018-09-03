
# importing flask modules
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
from googlesearch import search
import urllib3
import Google_search as gc
import Analysis as anyls
# initializing a variable of Flask
app = Flask(__name__)
bse=["Bse_Prc_tick_div","bse_upd_time","b_changetext"]


# decorating index function with the app.route with url as /login
@app.route('/')
def index():
   return render_template('login.html')

@app.route('/FlaskTutorial', methods = ['POST'])
def signup():
    q=[]
    com = request.form['company']
    dat = request.form['date']

    try:
        anyls.analyser(dat,com)
        imgnm= com + "_" + dat +".jpg"
        return render_template('success.html',imgnm=imgnm)
    except:
        d = open('/home/spanidea/.PyCharmCE2018.1/config/scratches/' + com + "_" + dat + '.txt', "w+")
        query = com + " share advanced chart moneycontrol"

        for j in search(query, tld="com", num=1, stop=1, pause=2):
            s = j
        URL = str(s)
        http = urllib3.PoolManager()
        r = http.request('GET', URL)
        soup = BeautifulSoup(r.data, 'html5lib')
        soup.prettify()
        for k in bse:
            content = soup.find("div", {"id": k})
            q.append(str(content.text))
            for div in content.findAll('img'):
                q.append(str(div)[46:116])
        d.write(str(q))
        d.write("\n")
        d.close()
        try:
            print "Tracking shares of " + com + " on " + str(dat)
            gc.runner(com,dat)
        except:
            print "See Plot in browser"
            imgnm = com + "_" + dat + ".jpg"
            return render_template('success.html', imgnm=imgnm)

 #   return redirect('login.html')


if __name__ == "__main__":
   app.run()
