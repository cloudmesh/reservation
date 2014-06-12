from flask import render_template


    return render_template('user/keys.html',
                           user=user_mongo,
                           show=msg)
