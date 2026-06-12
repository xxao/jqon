# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from dataclasses import dataclass


@dataclass
class Address(object):
    country: str = ""
    city: str = ""
    street: str = ""
    number: str = ""
    zip: str = ""


@dataclass
class Person(object):
    name: str = ""
    age: int = 0
    address: Address = None
    married: bool = False
    children: list = ()
    items: dict = None


A1 = Address(country="DW", city="Ankh-Morpork", street="Dimwell", number="23", zip="88888")
A2 = Address(country="ME", city="Shire", number="13", zip="13000")

P1 = Person(name="P1", age=10, address=A1, items={"lego": 100, "merkur": 2, "bike": 1})
P2 = Person(name="P2", age=7, address=A1, items={"lego": 57, "bike": 1})
P3 = Person(name="P3", age=50, address=A1, married=True, children=[P1, P2])
P4 = Person(name="P4", age=77, address=A2, married=True, children=[P3])
