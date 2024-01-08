from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

log_data_path = 'C:/Users/Bishal/PycharmProjects/LogAnalyzerTool/output.csv'
log_df = pd.read_csv(log_data_path)


def get_chart_data(selected_category):
    chart_data = log_df[selected_category].value_counts().to_dict()
    return chart_data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart_data/<selected_category>')
def fetch_chart_data(selected_category):
    data = get_chart_data(selected_category)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
