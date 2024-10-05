from dz_lib.u_pb.metrics import similarity, likeness
from flask import Flask, request, jsonify
from dz_lib.u_pb import metrics

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/uni/metrics/<metric>')
def u_pb_metrics(metric):
    json_data = request.json
    y1_values = json_data['y1_values']
    y2_values = json_data['y2_values']
    if metric == 'similarity':
        score = metrics.similarity(y1_values, y2_values)
    elif metric == 'likeness':
        score = metrics.likeness(y1_values, y2_values)
    elif metric == 'cross_correlation':
        score = metrics.r2(y1_values, y2_values)
    elif metric == 'ks':
        score = metrics.ks(y1_values, y2_values)
    elif metric == 'kuiper':
        score = metrics.kuiper(y1_values, y2_values)
    else:
        raise ValueError(f"Unknown metric '{metric}'")
    return jsonify({'metric': metric, 'score': score})

if __name__ == '__main__':
    app.run()
