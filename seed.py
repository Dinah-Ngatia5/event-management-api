from server import create_app, db
from server.models import User

app = create_app()
app.app_context().push()

def seed_db():
    users = [
        {'username': 'john_vick', 'email': 'john@gmail.com', 'password': 'password123'},
        {'username': 'dainah', 'email': 'dinahngatia86@gmail.com', 'password': 'password123'},
    ]

    for user_data in users:
        existing_user = User.query.filter_by(email=user_data['email']).first()
        if not existing_user:
            user = User(username=user_data['username'], email=user_data['email'])
            user.set_password(user_data['password'])
            db.session.add(user)
        else:
            print(f"User with email {user_data['email']} already exists.")

    db.session.commit()

if __name__ == '__main__':
    seed_db()
