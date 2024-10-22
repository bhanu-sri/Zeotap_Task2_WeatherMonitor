from flask import Flask, render_template
from data_processing import get_daily_summary, get_alerts

app = Flask(__name__)

@app.route('')
def index()
    summaries = get_daily_summary()
    alerts = get_alerts()
    return render_template('index.html', summaries=summaries, alerts=alerts)

if __name__ == '__main__'
    app.run(debug=True)
