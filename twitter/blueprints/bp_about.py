from flask import Blueprint, render_template

from util.location_util import woeid_to_location_map, location_models

about = Blueprint('about', __name__,
                  template_folder='templates')


@about.route("/about")
def show_about():
    locations = woeid_to_location_map()
    locations_by_parent = location_models()
    return render_template("about.html", map=locations, locations_by_parent=locations_by_parent)



