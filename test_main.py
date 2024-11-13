import pytest
from main import data_SMHI

def test_api_response():
    df, code = data_SMHI()
    
    # Kontrollera att API-anropet lyckades
    assert code == 200, f"Expected status code 200, but got {code}"
    
    # Kontrollera att dataformatet är korrekt
    assert not df.empty, "DataFrame should not be empty"
    assert "temperature" in df.columns, "DataFrame should contain 'temperature' column"
    assert "rainOrSnow" in df.columns, "DataFrame should contain 'rainOrSnow' column"

    print("API response and data format are correct")

