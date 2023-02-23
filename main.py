from flask import Flask, render_template, redirect, url_for
from data import db_session
from data.new_user import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init(f"db/blogs.db")
    db_sess = db_session.create_session()
    for user in db_sess.query(User).filter(User.address == 'module_2', User.speciality.notilike("%engineer%"),
                                           User.position.notilike("%engineer%")):
        print(user.id)

    db_sess.commit()


if __name__ == '__main__':
    main()