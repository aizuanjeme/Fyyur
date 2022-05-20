from models.db import db


class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key = True)
    start_time = db.Column(db.DateTime, nullable = False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    
    def __repr__(self) -> str:
        return f'<Show {self.id} {self.start_time} {self.venue_id} {self.artist_id} >'
