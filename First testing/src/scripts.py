import datetime as dt

def today():
  return dt.date.today().strftime('%A %B %d, %Y')

def compute_pi(n):
  pi = 2
  for i in range(1,n):
    pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
  return pi
