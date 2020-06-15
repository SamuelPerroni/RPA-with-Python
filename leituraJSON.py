import json

with open(r'.\Config\config.json') as config:    
    data = json.load(config)

sites = data['sites']
