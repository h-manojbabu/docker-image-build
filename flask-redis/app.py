from flask import Flask
import redis

app = Flask(__name__)

redis_client = redis.Redis(host='redis', port=6379)

@app.route('/')
def index():
    try:
        visits = redis_client.incr('counter')
        return f"""
        <h1>CloudOps Chronicle</h1>
        <h2>Docker Compose Demo</h2>
        <h3>Visits: {visits}</h3>
        """
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

