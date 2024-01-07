from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

log_data_path = 'C:/Users/Bishal/PycharmProjects/LogAnalyzerTool/src/output.csv'

log_df = pd.read_csv(log_data_path)


@app.route('/')
def index():
    data = log_df.head()
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
