from flask import Flask, render_template, request,session, redirect, url_for,flash,logging
from flask_mysqldb import MySQL
import os


app = Flask(__name__)
app.secret_key = '52\x04\xbd\xf7\xd7\xfe\xe9\x9akVZ~\xfa|\x06\xc2|(\xb5b\t\xd5d'

##mydb = mysql.connector.connect(host = "localhost",user = "root",password = "1234") 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'criLeagtur' 
mysql = MySQL(app) 




@app.route('/', methods=['GET', 'POST'])
def main():
    
    if request.method == "POST":
        details = request.form
        Country = details.get('country')
        Teams = details.get('teams')
        Venue = details.get('venue')
        Result = details.get('result')
        Player_Name= details.get('pname')
        Player_DOB = details.get('dob')
        Player_Skills = details.get('bob')
        Player_country = details.get('pcountry')
        Match_List = details.get('mlist')
        Team_Details = details.get('teamd')
        Winner = details.get('winner')
        Looser = details.get('looser')
        Man_Match = details.get('mm')
        Bowler_Match = details.get('mb')
        Best_Fielder = details.get('fb')
        Run = details.get('run')
        Wicket = details.get('wkt')
        Overs = details.get('overs')
        cur = mysql.connection.cursor()
        
        cur.execute("CREATE TABLE IF NOT EXISTS league(id int PRIMARY KEY AUTO_INCREMENT,Country Varchar(40),Teams Varchar(40),Venue Varchar(40),Result Varchar(40),Player_Name Varchar(40),Player_DOB Varchar(40),Player_Skills Varchar(40),Player_country Varchar(40),Match_List Varchar(40),Team_Details Varchar(40),Winner Varchar(40),Looser Varchar(40),Man_Match Varchar(40),Bowler_Match Varchar(40),Best_Fielder Varchar(40),Run Varchar(40),Wicket Varchar(40),Overs Varchar(40))")
        cur.execute("INSERT INTO league(Country,Teams,Venue,Result,Player_Name,Player_DOB,Player_Skills,Player_country,Match_List,Team_Details,Winner,Looser,Man_Match,Bowler_Match,Best_Fielder,Run,Wicket,Overs) VALUES (%s, %s, %s,%s, %s, %s,%s,%s, %s, %s,%s,%s, %s,%s,%s,%s,%s,%s)", (Country,Teams,Venue,Result,Player_Name,Player_DOB, Player_Skills ,Player_country,Match_List,Team_Details,Winner,Looser,Man_Match,Bowler_Match,Best_Fielder,Run,Wicket,Overs))
        mysql.connection.commit()
        cur.close()
        return render_template("main.html")
    return render_template("main.html")
        
                




@app.route('/search')
def search():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM league")
    data = cur.fetchall()
    cur.close()  
    return render_template('search.html', league=data )

@app.route('/search1')
def search1():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM league")
    data = cur.fetchall()
    cur.close()
    return render_template('search1.html', league=data )

    
    

@app.route('/update',methods=['POST','GET'])
def update():
    if request.method == 'POST':
        
        Player_Name= request.form['pname']
        Player_DOB = request.form['dob']
        Player_Skills = request.form['bob']
        Player_Country = request.form['pcountry']
        Match_List = request.form['mlist']
        Team_Details = request.form['teamd']
        Winner = request.form['winner']
        Looser = request.form['looser']
        Man_Match = request.form['mm']
        Bowler_Match = request.form['mb']
        Best_Fielder = request.form['fb']
        
        
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE league 
        SET  Player_DOB=%s, Player_Skills=%s, Player_Country=%s, Match_List=%s, Team_Details=%s, Winner=%s, Looser=%s, Man_Match=%s, Bowler_Match=%s, Best_Fielder=%s 
        WHERE Player_Name=%s 
        """, (Player_Name, Player_DOB, Player_Skills, Player_Country, Match_List, Team_Details, Winner, Looser, Man_Match, Bowler_Match,  Best_Fielder))
        flash("Details Updated Successfully","success")
        mysql.connection.commit()
        cur.close()
        return render_template("update.html")
    return render_template("update.html")    




@app.route('/delete/<string:b_data>', methods = ['GET'])
def delete(b_data):
    flash("Details Has Been Deleted Successfully","success")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM league WHERE id=%s", (b_data,))
    mysql.connection.commit()
    return redirect(url_for("search"))

                 

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000))))


    