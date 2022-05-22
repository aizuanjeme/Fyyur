from email.policy import default
from zoneinfo import available_timezones
from models.db import db


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    ###############################################################################
    website_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, nullable=False, default=False)
    seeking_description = db.Column(db.String())
    available = db.Column(db.Boolean, nullable=False, default=False)
    created_by = db.Column(db.DateTime, nullable = False)
    shows = db.relationship('Show', backref='artist')

    def __repr__(self) -> str:
        return f'<Artist {self.id} {self.name} >'
