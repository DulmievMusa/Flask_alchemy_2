from flask import Flask, render_template, redirect, url_for
from data import db_session
from data.new_user import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
db_session.global_init(f"db/blogs.db")
db_sess = db_session.create_session()


def main():
    app.run(port=8080, host='127.0.0.1')


@app.route("/")
def index():
    jobs = []
    for job in db_sess.query(Jobs).all():
        user = db_sess.query(User).filter(User.id == job.team_leader).first()
        name = user.surname + ' ' + user.name
        jobs.append((job.job, name, f'{job.work_size} hours', job.collaborators,
                     'Is finished' if job.is_finished else 'Is not finished'))
    return render_template("index.html", style=url_for('static', filename='css/style.css'), jobs=jobs)


if __name__ == '__main__':
    main()