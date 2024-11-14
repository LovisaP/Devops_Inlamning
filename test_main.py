from main import data_SMHI

def test_api_status_code():
    _, code = data_SMHI()
    assert code == 200, f"Expected status code 200, but got {code}"

def test_dataframe_not_empty():
    df, _ = data_SMHI()
    assert not df.empty, "DataFrame should not be empty"

def test_temperature_column_exists():
    df, _ = data_SMHI()
    assert "temperature" in df.columns, "DataFrame should contain 'temperature' column"

def test_rainOrSnow_column_exists():
    df, _ = data_SMHI()
    assert "rainOrSnow" in df.columns, "DataFrame should contain 'rainOrSnow' column"
