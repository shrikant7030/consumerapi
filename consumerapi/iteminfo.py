

class Item:

    def __init__(self,pid,pnm,prc,pqty):
        self.itemId = pid
        self.itemName = pnm
        self.itemPrice=prc
        self.itemQty = pqty

    def __str__(self):
        return f'''\n Id : {self.itemId} , Name : {self.itemName} , Price : {self.itemPrice} , Qty : {self.itemQty}'''

    def __repr__(self):
        return str(self)