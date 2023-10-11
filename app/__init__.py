from flask import Flask, render_template
from .config import Config

# ----------- Application Imports ----------- #
from .extensions import socketio


# ----------- Register Blueprints ----------- #
def register_blueprints(app):
    from .chat.routes import chat
    from .auth.routes import auth

    app.register_blueprint(chat)
    app.register_blueprint(auth)


# ----------- Register Extensions ----------- #
def register_extensions(app):
    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    ckeditor.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)


# ----------- Context Processors and Error Handlers ----------- #
def apply_themes(app):
    ## Error Handling
    # Invalid URL Error Handler
    @app.errorhandler(404)
    def page_not_found(e):
        # return render_template('404.html', error=e), 404
        return render_template('404.html', error=e), 404

    # Internal Server Error
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html', error=e), 500

    ## Jinja Function
    # @app.context_processor
    # def context_processor():
    #     return dict(
    #             siteName = func['siteName'],
    #             siteUrl = func['siteUrl'],
    #             getCategoryName = func['getCategoryName']
    #         )


# ----------- Initialize the core application ----------- #
def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config())
    # Instantiate Flask application

    with app.app_context():
        register_blueprints(app)
        # register_extensions(app)
        apply_themes(app)

        return app