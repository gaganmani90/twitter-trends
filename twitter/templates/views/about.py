from flask import Blueprint, render_template

about = Blueprint('about', __name__,
                  template_folder='templates',
                  static_folder='templates/static')


@about.route("/about")
def show_about():
    return render_template("about.html")
