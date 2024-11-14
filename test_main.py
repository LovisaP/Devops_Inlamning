from main import data_SMHI

def test_api_status_code():
    df = data_SMHI()
    assert df is not None, "Expected data_SMHI() to return a DataFrame, but got None"

def test_dataframe_not_empty():
    df = data_SMHI()
    assert not df.empty, "DataFrame should not be empty"

def test_temperature_column_exists():
    df = data_SMHI()
    assert "temperature" in df.columns, "DataFrame should contain 'temperature' column"

def test_rainOrSnow_column_exists():
    df = data_SMHI()
    assert "rainOrSnow" in df.columns, "DataFrame should contain 'rainOrSnow' column"
