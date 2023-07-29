from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/terms-of-service')
def terms_of_service():
    return render_template('terms-of-service.html')


@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy-policy.html')


@app.route('/8f9e02a142c704757466060cf57d4552.html')
def host():
    return render_template('8f9e02a142c704757466060cf57d4552.html')


if __name__ == '__main__':
    app.run(debug=True)
