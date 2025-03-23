from typing import Any, Dict, List
import io
import pandas as pd
import requests


@data_loader
def get_mtg_cards(**kwargs: Any) -> pd.DataFrame:
        
    api_url = "*********************************"

    response = requests.get(api_url)

    return pd.read_csv(io.StringIO(response.text), sep=',')

def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

