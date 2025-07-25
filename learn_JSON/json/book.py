book={}
book['Ravi'] = {
    'name':'Ravi',
    'Address':"Inderwa,koderma,825410",
    'Mobile_number':9199992833

}
book["Rishi"]={
    'name': 'Rishi',
    'Address': 'Domchanch,825418',
    'Mobile_number': 7479911592

}

import json
r=json.dumps(book)
print(r)
