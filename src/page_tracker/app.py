import os
from functools import cache
from redis import Redis, RedisError
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


@app.get("/")
def index():
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")
    else:
        return f"This page has been seen {page_views} times."


# for singleton, only one instance of client in memory
@cache
def redis():
    return Redis.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379/"))
    # return Redis(
    #     host=os.environ.get("REDIS_HOST", "localhost"),
    #     port=os.environ.get("REDIS_PORT", 6379),
    # )
