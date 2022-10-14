import datetime
from peewee import Model, DateField

def sorting(DB):
  class Orders(Model):
    created_at = DateField()
    class Meta:
      database = DB
  
  today = datetime.datetime.now()

  dateIn = datetime.date(today.year, today.month - 1, today.day)

  onSorting = Orders.select().where(Orders.created_at > dateIn)

  return onSorting
