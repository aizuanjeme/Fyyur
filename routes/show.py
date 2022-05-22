from flask import Blueprint, render_template
from . import routes
from models.showModel import Show

show = Blueprint('show', __name__, template_folder='templates')


@routes.route('/shows', methods=['GET'])
def shows():
    # displays list of shows at /shows
    # TODO: replace with real venues data.
     data = []
     shows = Show.query.all()
     for show in shows:
         data.append({
             "venue_id": show.venue_id,
             "venue_name": show.venue.name,
             "artist_id": show.artist_id,
             "artist_name": show.artist.name,
             "artist_image_link": show.artist.image_link if show.artist.image_link!="" else "https://www.emergingedtech.com/wp/wp-content/uploads/2017/04/Music.jpg",
             "start_time": show.start_time.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
          })
     return render_template('pages/shows.html', shows=data)
