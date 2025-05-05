import pytest

from app_test.db import Database

@pytest.fixture
def db():
    test_db = Database(":memory:")
    yield test_db
    test_db.close()


def test_add_user(db):
    db.add_user("Alice")
    users = db.get_all_users()
    assert len(users) == 1
    assert users[0][1] == "Alice"


def test_multiple_users(db):
    db.add_user("Alice")
    db.add_user("Bob")
    users = db.get_all_users()
    names = [user[1] for user in users]
    assert "Alice" in names
    assert "Bob" in names
    assert len(users) == 2


def test_empty_users(db):
    users = db.get_all_users()
    assert users == []