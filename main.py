#!/usr/bin/env python3
from datetime import date, timedelta
from forex_python.converter import CurrencyRates
from time import sleep
from os.path import abspath, dirname, exists, join

DIR = dirname(abspath(__file__))


def main():
  c = CurrencyRates()
  today = date.today()

  currency = "CNY"

  csvfile = join(DIR, currency + ".csv")

  pre = None

  if exists(csvfile):
    with open(csvfile) as f:
      for i in f:
        i = i.strip("\n")
        if i:
          pre = i

  if not pre:
    pre = date(2008, 1, 1)
  else:
    pre = date(*map(int, pre.split(",",1)[0].split("-")))

  if today > pre:
    with open(csvfile, "a") as f:
      while today > pre:
        pre = pre + timedelta(days=1)
        cny = c.get_rates('USD', pre)['CNY']
        f.write(f"{str(pre)},{cny}\n")
        f.flush()
        print(pre, cny)


main()
