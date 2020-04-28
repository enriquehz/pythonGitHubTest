dict = { "country": ["Brazil", "Russia", "India", "China", "South Africa"],
       "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "area": [8.516, 17.10, 3.286, 9.597, 1.221],
       "population": [200.4, 143.5, 1252, 1357, 52.98] }

import json
import pandas as pd

def lambda_handler(event, context):
    # TODO implement
    brics = pd.DataFrame(dict)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello world from lambda')
    }
    
    
    


