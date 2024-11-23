from flask import Flask, render_template_string
import threading
import time

app = Flask(__name__)

# HTML template for the reminders
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Health Reminder App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            text-align: center;
            background-color: #f4f4f9;
        }
        h1 {
            color: #3498db;
        }
        .reminder {
            border: 1px solid #ddd;
            margin: 20px;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }
    </style>
</head>
<body>
    <h1>💧 Health Reminder App 💧</h1>
    <div class="reminder">
        <h2>Water Reminder</h2>
        <p>Don't forget to drink a glass of water!</p>
    </div>
    <div class="reminder">
        <h2>Stand-Up Reminder</h2>
        <p>Get up, stretch, and move around for a bit!</p>
    </div>
    <div class="reminder">
        <h2>Daily Exercise Reminder</h2>
        <p>Remember: Exercise is key to staying strong and healthy!</p>
    </div>
    <p>(This page will refresh every hour for water and stand-up reminders!)</p>
</body>
</html>
"""


# Route for the main page
@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)


# Background task to print reminders to the console
def background_reminder():
    while True:
        print("💧 Time to drink water!")
        print("🧍 Time to stand up and stretch!")
        time.sleep(3600)  # Wait for one hour


# Start the background thread for reminders
reminder_thread = threading.Thread(target=background_reminder, daemon=True)
reminder_thread.start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
