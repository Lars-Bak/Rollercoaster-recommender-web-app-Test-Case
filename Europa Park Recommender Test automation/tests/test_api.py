import pytest
from config import ALLOWED_COASTERS

# ---------------------------------------------------------
# 1. GET /recommender must show the first step
# ---------------------------------------------------------
def test_recommender_get(client):
    response = client.get("/recommender")
    assert response.status_code == 200
    assert b"length" in response.data  # the first step


# ---------------------------------------------------------
# 2. POST no length → error page
# ---------------------------------------------------------
def test_recommender_missing_length(client):
    response = client.post("/recommender", data={})
    assert response.status_code == 200

    # The app shows the first step of the flow again
    assert b"length" in response.data



# ---------------------------------------------------------
# 3. POST with unrealistic length → error page
# ---------------------------------------------------------
def test_recommender_invalid_length(client):
    response = client.post("/recommender", data={"length": "abc"})
    assert response.status_code == 200
    assert b"Invalid" in response.data or b"unrealistic" in response.data


# ---------------------------------------------------------
# 4. POST too short → error message
# ---------------------------------------------------------
def test_recommender_too_short(client):
    response = client.post("/recommender", data={"length": "90"})
    assert response.status_code == 200
    assert b"Too short" in response.data


# ---------------------------------------------------------
# 5. POST with length for young_kids_recommender
# ---------------------------------------------------------
def test_recommender_young_kids(client):
    response = client.post("/recommender", data={"length": "110"})
    assert response.status_code == 200
    # check for a piece of HTML that returns young_kids_recommender
    assert b"kids" in response.data or b"recommend" in response.data


# ---------------------------------------------------------
# 6. POST with length for intense_recommender
# ---------------------------------------------------------
def test_recommender_intense(client):
    response = client.post("/recommender", data={"length": "135"})
    assert response.status_code == 200
    assert b"intense" in response.data or b"recommend" in response.data


# ---------------------------------------------------------
# 7. POST too long → error message
# ---------------------------------------------------------
def test_recommender_too_tall(client):
    response = client.post("/recommender", data={"length": "210"})
    assert response.status_code == 200
    assert b"Too tall" in response.data

# ---------------------------------------------------------
# 8. POST with Rollercoasters as a recommendation
# ---------------------------------------------------------
@pytest.mark.parametrize("coaster", ALLOWED_COASTERS)
def test_all_coaster_pages(client, coaster):
    response = client.get(f"/coaster/{coaster}")
    assert response.status_code == 200
    assert coaster.encode() in response.data

# ---------------------------------------------------------
# 9. POST with expected length and recommender
# ---------------------------------------------------------
@pytest.mark.parametrize("length,expected_function", [
    (110, "young_kids"),
    (125, "kids"),
    (135, "intense"),
    (150, "high"),
])
def test_recommender_paths(client, length, expected_function):
    response = client.post("/recommender", data={"length": str(length)})
    assert response.status_code == 200
    assert expected_function.encode() in response.data


def test_coaster_page_unknown(client):
    response = client.get("/coaster/OnbekendeCoasterXYZ")
    assert response.status_code == 404

# ---------------------------------------------------------
# Report command
# pytest --html=report.html --self-contained-html
# ---------------------------------------------------------
