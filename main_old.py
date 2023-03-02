from flask import Flask, render_template, redirect, url_for
from data import db_session
from data.new_user import User
from data.news import News
from forms.user import RegisterForm
from loginform import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


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


@app.route('/training/<prof>')
def training(prof):
    return render_template('base.html', title=prof, prof=prof, first_img=url_for('static', filename='img/first.jpeg'),
                           second_img=url_for('static', filename='img/second.jpg'),
                           style=url_for('static', filename='css/style.css'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form, style=url_for('static', filename='css/style.css'),
                           log_image=url_for('static', filename='img/mars_emblem.png'))


@app.route('/list_prof/<lis>')
def list_prof(lis):
    sp = ['Медик', 'Инженер', 'Учёный', 'Болтун', 'Шут']
    return render_template('index.html', sp=sp, arg=lis, style=url_for('static', filename='css/style.css'))


@app.route('/answer')
def answer():
    params = {
        'title': 'Анкета',
        'surname': 'Утопия',
        'name': 'Шоу',
        'education': 'Высшее гитарное',
        'profession': 'Блогер',
        'sex': 'male',
        'motivation': 'Снять Топ Сикрет',
        'ready': 'True',
        'style': url_for('static', filename='css/style.css')
    }
    return render_template('auto_answer.html', **params)


@app.route('/auto_answer')
def auto_answer():
    params = {
        'title': 'Анкета',
        'surname': 'Утопия',
        'name': 'Шоу',
        'education': 'Высшее гитарное',
        'profession': 'Блогер',
        'sex': 'male',
        'motivation': 'Снять Топ Сикрет',
        'ready': 'True',
        'style': url_for('static', filename='css/style.css')
    }
    return render_template('auto_answer.html', **params)


@app.route('/distribution')
def distribution():
    return render_template('by_cabins.html', style=url_for('static', filename='css/style.css'),
                           sp=['Ридли Скотт', 'Валера', 'Кто-то', 'Василий', 'Хых Хах Ын'])


@app.route('/table/<sex>/<age>')
def top_kayota(sex, age):
    if int(age) < 21:
        photo = url_for('static', filename='img/small_mars.jpeg')
        if sex == 'male':
            wall = url_for('static', filename='img/male-small.jpg')
        else:
            wall = url_for('static', filename='img/fem_small.jpg')
    else:
        photo = url_for('static', filename='img/old.png')
        if sex == 'male':
            wall = url_for('static', filename='img/male-old.jpg')
        else:
            wall = url_for('static', filename='img/fem_old.jpeg')

    return render_template('top_kayota.html', style=url_for('static', filename='css/style.css'),
                           photo=photo, wall=wall)


if __name__ == '__main__':
    main()