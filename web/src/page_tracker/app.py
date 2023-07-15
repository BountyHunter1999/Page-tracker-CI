import os
from functools import cache

from flask import Flask
from redis import Redis, RedisError

app = Flask(__name__)


@app.get("/")
def index():
    try:
        page_views = redis().incr("page_views")
    except RedisError:
        app.logger.exception("Redis error")  # pylint: disable=E1101
        return "Sorry, something went wrong \N{pensive face}", 500
    else:
        return f"This page has been seen {page_views} times."


# for singleton, only one instance of client in memory
@cache
def redis():
    return Redis.from_url(
        os.environ.get("REDIS_URL", "redis://localhost:6379/")
    )  # noqa: E501
    # return Redis(
    #     host=os.environ.get("REDIS_HOST", "localhost"),
    #     port=os.environ.get("REDIS_PORT", 6379),
    # )


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
