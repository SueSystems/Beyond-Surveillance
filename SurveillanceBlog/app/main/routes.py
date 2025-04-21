from app.main import bp

@bp.route('/')
@bp.route('/index')
def index():
    """Home page of the SurveillanceBlog."""
    return "welcome to SurveillanceBlog!"
