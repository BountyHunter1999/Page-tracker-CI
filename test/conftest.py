"""
Contains common fixtures that are used by different
types of tests
"""
import pytest
import redis

from page_tracker.app import app


@pytest.fixture
def http_client():
    return app.test_client()


# module to reuse the same Redis client instance for all within a
# test module
@pytest.fixture(scope="module")
def redis_client():
    return redis.Redis()
