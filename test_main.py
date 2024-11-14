from main import data_SMHI

def test_api_status_code():
    _, code = data_SMHI()
    assert code == 200, f"Expected status code 200, but got {code}"

def test_time_series_exists():
    data, _ = data_SMHI()
    assert "timeSeries" in data, "timeSeries not found in API response"

def test_time_series_not_empty():
    data, _ = data_SMHI()
    assert len(data["timeSeries"]) > 0, "timeSeries is empty in API response"

def test_parameters_in_time_series():
    data, _ = data_SMHI()
    assert "parameters" in data["timeSeries"][0], "Parameters missing in timeSeries"
    assert len(data["timeSeries"][0]["parameters"]) > 0, "No parameters in timeSeries"

