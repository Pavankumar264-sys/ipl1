from flask import Flask,render_template
from utils.db import db
from models.add import *




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///add.db'
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/players')
def home():
    players = IPLPlayer.query.all()
    return render_template('players.html', content=players)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    player_id = form_data.get('player_id')
    player_name = form_data.get('player_name')
    team = form_data.get('team')
    matches_played = form_data.get('matches_played')
    runs_scored = form_data.get('runs_scored')
    wickets_taken = form_data.get('wickets_taken')

    # Check if the player already exists
    player = IPLPlayer.query.filter_by(player_id=player_id).first()
    if not player:
        # Create a new IPLPlayer instance
        player = IPLPlayer(
            player_id=player_id,
            player_name=player_name,
            team=team,
            matches_played=matches_played,
            runs_scored=runs_scored,
            wickets_taken=wickets_taken,
        )
        db.session.add(player)
        db.session.commit()
    print("Submitted successfully")
    return redirect('/players')

@app.route('/teams')
def teams():
    return render_template('teams.html')


@app.route('/matches')
def matches():
    return render_template('matches.html')


@app.route('/table')
def table():
    return render_template('table.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/news')
def news():
    return render_template('news.html')




if __name__=='__main__':
    app.run(
        host='127.0.0.1',
        port=4005,
        debug=True

    )