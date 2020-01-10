from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors
from ..models import Permission


# Adding the Permission class to the template context
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)
