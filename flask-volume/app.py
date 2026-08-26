from flask import Flask
import os

app = Flask(__name__)

COUNTER_FILE = "/data/counter.txt"

@app.route('/')
def home():

    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, "w") as f:
            f.write("0")

    with open(COUNTER_FILE, "r") as f:
        count = int(f.read())

    count += 1

    with open(COUNTER_FILE, "w") as f:
        f.write(str(count))

    return f"""
    <h1>CloudOps Chronicle</h1>
    <h2>Docker Volume Demo</h2>
    <h3>Visits: {count}</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
