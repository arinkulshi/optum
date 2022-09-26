import json

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    del state['area_code']

'''
Anthony: Recrutier
Jesse: FE 
David Law : BE 
Rick Bassham : System Design
Tommy Hickey : Product
Joe : Hiring Manager
'''


