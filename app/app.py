from flask import Flask 
from website import website_pages_blueprint,home_blueprint #所有網頁

from config import FLASK_STATIC_DIR, UPLOAD_FOLDER



def create_app():#Application Factories
    app = Flask(__name__, 
                static_url_path='/static/', 
                static_folder=FLASK_STATIC_DIR)
    
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


    app.register_blueprint(website_pages_blueprint)
    app.register_blueprint(home_blueprint)

    ###API###
    
    return app
