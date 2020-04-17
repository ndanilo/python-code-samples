def defineDb(_db):
    db = _db
    subs = db.Table('Subs',
            db.Column('User_Id', db.BigInteger(), db.ForeignKey('Players.Id')),
            db.Column('Channel_Id', db.BigInteger(), db.ForeignKey('Channels.Id'))
        )
    class Definitions:
        class Wallet(db.Model):
            __tablename__ = 'Wallets'
            id = db.Column('Id', db.BigInteger(), primary_key=True)
            name = db.Column('Name',db.String(50))
            player_id = db.Column('Player_Id', db.BigInteger(), db.ForeignKey('Players.Id'), unique=True)
            player = db.relationship('Player', uselist=False)

        class Player(db.Model):
            __tablename__='Players'
            id = db.Column('Id', db.BigInteger, primary_key=True)
            name = db.Column('Name', db.String(50))
            clubs = db.relationship('Club', backref='player', lazy='dynamic')
            #subscriptions = db.relationship('Channel', secondary=subs,backref=db.backref('subscribers'), lazy='dynamic')
            subscriptions = db.relationship('Channel', secondary=subs, lazy='dynamic')
            wallet = db.relationship('Wallet', uselist=False)

            def __init__(self, name):
                self.name = name

        class Club(db.Model):
            __tablename__ = 'Clubs'
            id = db.Column('Id', db.BigInteger, primary_key=True)
            name = db.Column('Name', db.String(50), unique=True)
            player_id = db.Column('Player_Id', db.BigInteger, db.ForeignKey('Players.Id'))

            def __init__(self, name, player):
                self.name = name
                self.player = player

        class Channel(db.Model):
            __tablename__ = 'Channels'
            id = db.Column('Id', db.BigInteger(), primary_key=True)
            name = db.Column('Name', db.String(50))
            subscribers = db.relationship('Player', secondary=subs, lazy='dynamic')
            
            def __init__(self, name):
                self.name = name

        class Log(db.Model):
            __tablename__ = 'Logs'
            id = db.Column('Id', db.BigInteger(), primary_key=True)
            message = db.Column('Message', db.String(50))
            
            def __init__(self, message):
                self.message = message

    return Definitions()