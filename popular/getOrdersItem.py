from peewee import *
from .sortedByDate import sorting

def getOrders(DB):

  datas = []

  class OrderItems(Model):
    order_id = IntegerField()
    product_id = IntegerField()
    quantity = DoubleField()

    class Meta:
      database = DB
      legacy_table_names = False

  for item in sorting(DB):
    datas.append(item.id)
  
  getData = OrderItems.select().where((OrderItems.order_id << datas)
                                      & (OrderItems.product_id != None))

  return getData
