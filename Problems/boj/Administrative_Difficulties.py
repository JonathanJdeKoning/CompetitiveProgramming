from collections import defaultdict
from dataclasses import dataclass
from math import floor, ceil
@dataclass
class Car:
    price: int
    pickup: int
    kilo: int

@dataclass
class Spy:
    total: int 
    curr: str
    good: bool

for tc in range(int(input())):
    n,m = list(map(int, input().replace(","," ").split()))
    cars = {}
    people = {}
    for _ in range(n):
        car, price, pickup, kilo = input().split()
        price = int(price)
        pickup = int(pickup)
        kilo = int(kilo)
        cars[car] = Car(price, pickup, kilo)
    
    for _ in range(m):
        time, name, op, car = input().split()
        if name not in people:
            people[name] = Spy(0, None, True)
        spy = people[name]
        if not spy.good: continue
        if op == "p":
            if spy.curr:
                spy.good = False
                continue
            spy.total += cars[car].pickup
            spy.curr = car
        elif op == "r":
            if not spy.curr:
                spy.good = False
                continue
            spy.total += cars[spy.curr].kilo*int(car)
            spy.curr = None
        elif op == "a":
            if not spy.curr:
                spy.good = False
                continue
            spy.total += ceil(cars[spy.curr].price * (int(car)/100))
    for spy in sorted(people.keys()):
        if not people[spy].good or people[spy].curr:
            print(spy, "INCONSISTENT")
        else:
            print(spy, people[spy].total)





