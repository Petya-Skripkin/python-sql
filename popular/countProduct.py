from collections import Counter
from .getOrdersItem import getOrders

def countProduct(DB):
  counts = []
  for item in getOrders(DB):
    i = 0
    while i < item.quantity:
      i += 1
      counts.append(item.product_id)

  listing = Counter(counts)
  res = []

  for item in listing.keys():
    if listing[item] > 2:
      res.append(item)

  return res
