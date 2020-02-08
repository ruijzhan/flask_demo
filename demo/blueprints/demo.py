from flask import Blueprint

demo_bp = Blueprint('demo', __name__)

@demo_bp.route('/')
def index():
    return 'This is a Blueprint page'