
def check_key(data,key_to_mask):
    if  key_to_mask in data :
        data[key_to_mask] = "****"

    else:
        if data not in {list,str}:
            for key_data,value_data in data.items():
                if isinstance(value_data, dict):
                    check_key(value_data,key_to_mask)
        if data is list:
            for value_data in data:
                check_key(value_data,key_to_mask)


def mask_key_value(data,key_to_mask):
    check_key(data,key_to_mask)
    print(data)

key_to_mask = "city"

data = {
  "isbn": "123-456-222",
  "author": {
    "lastname": "Doe",
    "firstname": "Jane",
    "address": {
      "city": "blr"
    },
    "address_history": [
      {
          "city": "blr"
       },
      {
          "city": "delhi"
       },
    ]
  },
  "editor": {
    "lastname": "Smith",
    "firstname": "Jane"
  },
  "title": "test"
}


mask_key_value(data,key_to_mask)



