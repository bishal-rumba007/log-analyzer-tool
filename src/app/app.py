from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

log_data_path = 'C:/Users/Bishal/PycharmProjects/LogAnalyzerTool/output.csv'
log_df = pd.read_csv(log_data_path)


# Your data fetching logic goes here
def get_chart_data(selected_category):
    if selected_category == 'Country':
        chart_data = log_df['Country'].value_counts().to_dict()
    elif selected_category == 'Browser':
        chart_data = log_df['Browser'].value_counts().to_dict()
    elif selected_category == 'DateTime':
        # Assuming 'Date Time' is a datetime column in your CSV
        chart_data = log_df['Date Time'].dt.year.value_counts().to_dict()
    elif selected_category == 'OperatingSystem':
        chart_data = log_df['Operating System'].value_counts().to_dict()
    else:
        chart_data = {}

    return chart_data


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/chart_data/<selected_category>')
def fetch_chart_data(selected_category):
    data = get_chart_data(selected_category)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
