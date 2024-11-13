import pytest
from main import data_SMHI

def test_api_response():

    df = data_SMHI()


    assert not df.empty, "DataFrame should not be empty"


    assert "temperature" in df.columns, "DataFrame should contain 'temperature' column"
    assert "rainOrSnow" in df.columns, "DataFrame should contain 'rainOrSnow' column"

    print("Data format and content are correct")

