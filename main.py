#!/usr/bin/python3
from models import storage
from models.state import State


states = storage.all(State)

for state in states.values():
    print(f"* {state.id} : {state.name}")
    for city in state.cities:
        print(f"\t - {city.id} : {city.name}")
