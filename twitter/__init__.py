import matplotlib
from flask import Flask
from flask_jsglue import JSGlue

from twitter.templates.views.about import about
from twitter.templates.views.home import home
from twitter.templates.views.image import chart
matplotlib.use('Agg')

app = Flask(__name__, static_folder='templates/static', template_folder='templates')
app.register_blueprint(chart)  # produce chart
app.register_blueprint(home)  # home page
app.register_blueprint(about)  # about page
jsglue = JSGlue(app)