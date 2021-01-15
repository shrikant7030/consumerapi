
# tamil --> application     --->            producer --> eng-- TRAIN --> [JSON]
#MARATHI               --> MARATHI --
#HINDI -->HINDI     --> CONSUMER -->

import requests
from newconsumer.consumerapi.iteminfo import Item

PRODUCER_URI = "http://localhost:8081/api/product/"


def serialize(item):
    prodjson = {
        "name": item.itemName,
        "price": item.itemPrice,
        "quantity": item.itemQty,
        "active": True
    }
    return prodjson


def deserialize(prodjson):
    if type(prodjson)==list:
        itemlist = []
        for prod in prodjson:
            itemlist.append(Item(pid=prod.get('id'),pnm=prod.get('name'),prc=prod.get('price'),pqty=prod.get('quantity')))
        return itemlist
    elif type(prodjson)==dict:
        prod = prodjson
        return Item(pid=prod.get('id'),pnm=prod.get('name'),prc=prod.get('price'),pqty=prod.get('quantity'))
        

def get_all_products():
    resp = requests.get(PRODUCER_URI)

    return deserialize(resp.json())

def get_product(pid):
    resp = requests.get(PRODUCER_URI+str(pid))
    if resp.status_code==200:
        return deserialize(resp.json())
    else:
        return "No Product Avaiable"

def add_new_product(prod):
    prod_json = serialize(prod)
    resp = requests.post(PRODUCER_URI,json=prod_json)
    print('status code : ', resp.status_code, "Response :", resp.json())
    if resp.status_code==201:

        return "Product Added Successfully...! {}".format(resp.json().get('id'))

def delete_product_api(pid):
    resp = requests.delete(PRODUCER_URI+str(pid)+"/")
    print('status code : ', resp.status_code)
    if resp.status_code == 204:
        return "Product Deleted"
    else:
        return "No Product with Given Id"



def update_product(pid,prod):
    prod_json = serialize(prod)
    resp = requests.put(PRODUCER_URI+str(pid)+"/",json=prod_json)
    print('status code : ', resp.status_code, "Response :", resp.json())
    if resp.status_code==200:
        return deserialize(resp.json())
    else:
        return "No Product with Given Id"


if __name__ == '__main__':
    pass
