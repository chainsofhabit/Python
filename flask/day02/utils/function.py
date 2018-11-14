from flask import url_for, session,redirect


def check(func):
    def check_login():

        try:
            session['user_id']
        except Exception as e:
            return redirect(url_for('user.login'))

        return func()

    return check_login


