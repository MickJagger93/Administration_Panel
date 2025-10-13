from flask import Blueprint, render_template, get_flashed_messages

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():

    messages = get_flashed_messages()
    return render_template('layouts/partials/public.html', messages=messages)