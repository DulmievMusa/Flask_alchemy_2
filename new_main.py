from flask import Flask, redirect, url_for, render_template
from data.db_session import SqlAlchemyBase
from data import db_session
from data.new_user import User
from forms.user import RegisterForm
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    db_session.global_init('db/blogs.db')
    db_sess = db_session.create_session()
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                           style=url_for('static', filename='css/style.css'), message="Пароли не совпадают")

        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                           style=url_for('static', filename='css/style.css'), message="Такой пользователь уже есть")
        user = User(
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
            email=form.email.data,
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/success')
    return render_template('register.html', title='Регистрация', form=form,
                           style=url_for('static', filename='css/style.css'))


@app.route('/success')
def success():
   return 'logged in successfully'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')