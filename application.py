from flask import Flask, render_template, request, url_for, jsonify, send_file, redirect
from predictor import Predictor
from state import State

# initialize flask app
app = Flask(__name__)

# initialize the predictor object
predictor = Predictor()

# intialize the state tracker object
state = State()

# routing functionality for root url
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # update the current state
        state.updateState(request)
        # make prediction using model
        pred = predictor.predict(request)
        # update the result in current state
        state.state['result'] = 'NO :(' if pred[0] == 0 else 'YES!'
        # rerender template with updated states
        return render_template('index.html', state=state.state)
    else:
        return render_template('index.html', state=state.state)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

