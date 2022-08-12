from flask import Blueprint


user_bp = Blueprint('user_bp', __name__)
users = [{
    "id": "1",
    "first_name": "test_first_name_1",
    "last_name": "test_last_name_1"
}, {
    "id": "2",
    "first_name": "test_first_name_2",
    "last_name": "test_last_name_2"
}]

@user_bp.route('/users', methods=['GET'], endpoint='get_users')
def get_users():

    return {
        "users": users
    }
