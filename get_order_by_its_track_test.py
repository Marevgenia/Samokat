import sender_stand_request
import data

#Test
def test_get_order_by_its_track():
    create_order_response = sender_stand_request.create_order(data.create_order_body)
    assert create_order_response.status_code == 201
    track_number = create_order_response.json()["track"]
    assert track_number != ""
    get_order_response = sender_stand_request.get_order_by_its_track(track_number)
    assert get_order_response.status_code == 200