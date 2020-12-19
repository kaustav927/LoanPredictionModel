import requests
import json
import jsonify


url = 'http://127.0.0.1:5000/predict/'

['Income','CreditScore','Debt','LoanTerm','InterestRate','CreditIncidents','HomeValue','LoanAmount',
               'Lat','Long','MedianHomeValue','MedianHouseholdIncome']

data = [[0, 10, 32000, 480, 0.1, 100, 561000, 3366600, 41.84568, -74.36764, 255000, 56444]]
data2 =[[473902, 784, 33173.14, 360, 0.038, 6, 380520, 304416, 46.32374, -120.00865, 135900, 44563]]
data3 = [[194940, 687, 74077.2, 480, 0.041, 0, 494260, 296556, 34.06635, -84.67837, 190100, 75421]]

# reject
data4 = [[52655,672,26327.5,420,0.039,5,1119420,335826,40.63316,-74.13653,414600,61925]]

# approve
data5 = [[894604,792,134190.6,420,0.039,0,136080,27216,35.25064,-91.73625,48600,30060]]

obj = {
  "income": "894604",
  "creditScore": "792",
  "debt": "134190.6",
  "loanTerm": "420",
  "interestRate": "0.039",
  "creditIncidents": "0",
  "homeValue": "136080",
  "loanAmount": "27216",
  "lat": "35.25064",
  "long": "-91.73625",
  "medianHomeValue": "48600",
  "medianHouseholdIncome": "30060"
}

j_data = json.dumps(obj)

headers = {'Content-Type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)