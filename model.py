from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Game(db.Model):
    """Board game."""

    __tablename__ = "games"
    game_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    description = db.Column(db.String(100))


def connect_to_db(app, db_uri="postgresql:///games"):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    db.app = app
    db.init_app(app)


def example_data():
    """Create example data for the test database."""
    # FIXME: write a function that creates a game and adds it to the database.

    Game.query.delete()

    apple = Game(name = "apples to apple", description = "card game")
    madlibs = Game(name = "madlibs", description = "wacky word game")
    scrabble = Game(name = "scrabble", description = "word game")

    db.session.add_all([apple, madlibs, scrabble])
    db.session.commit()



if __name__ == '__main__':
    from party import app

    connect_to_db(app)
    db.create_all()
    # example_data()
    print("Connected to DB.")
