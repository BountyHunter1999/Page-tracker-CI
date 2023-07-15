"""
Contains common fixtures that are used by different
types of tests
"""
import pytest
import redis

from page_tracker.app import app


# Customm command line arguments, that will be wrapped with session
# scoped fixtures
def pytest_addoption(parser):
    parser.addoption("--flask-url")
    parser.addoption("--redis-url")


# Session scoped fixtures, which will be injected into our test functions
# other fixtures
@pytest.fixture(scope="session")
def flask_url(request):
    return request.config.getoption("--flask-url")


@pytest.fixture(scope="session")
def redis_url(request):
    return request.config.getoption("--redis-url")


@pytest.fixture
def http_client():
    return app.test_client()


# module to reuse the same Redis client instance for all within a
# test module
@pytest.fixture(scope="module")
def redis_client(redis_url):
    if redis_url:
        return redis.Redis.from_url(redis_url)
    return redis.Redis()

