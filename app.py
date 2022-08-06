from urllib import request
import redis
from flask import Flask, redirect, url_for, request
import uuid

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'POST':
        num = uuid.uuid4()
        # print(request.form['nm'])
        cache.set(str(num), str(request.form['nm']))
        return redirect(url_for('done', value="generated id : " + str(num)
                                                + " and value : " + str(request.form['nm'])))
    else:
        # print("get----->", request.args.get('nm'))
        user = cache.get(request.args.get('nm'))
        return redirect(url_for('done', value=user))


@app.route('/done/<value>')
def done(value):
    return '%s' % value


if __name__ == '__main__':
    app.run(debug=True)
