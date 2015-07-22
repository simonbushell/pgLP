from flask import (Blueprint, request, render_template, flash, url_for,
                    redirect, session)

blueprint = Blueprint('public', __name__, static_folder="../static")

@blueprint.route("/")
def home():
	return "<body>hello world</body>"