#!/usr/bin/python
import numpy as np
import random as rnd

def get_value(value_map, state):
    if str(state) in value_map:
        return value_map[str(state)]
    else:
        return 0

def check_won(state, side):
    for i in range(0,3):
        if (state[i, :] == side).all():
            return True
        if (state[:, i] == side).all():
            return True
    if (state.diagonal() == side).all():
        return True
    if (np.fliplr(state).diagonal() == side).all():
        return True
    return False

def choose_next_random(state, side):
    non_filled_count = 9 - np.count_nonzero(state)
    if non_filled_count == 0:
        return False
    pos = rnd.randint(0, non_filled_count - 1)
    index = 0
    for i in range(0,3):
        for j in range(0,3):
            if state[i, j] == 0:
                if index == pos:
                    state[i, j] = side
                index = index + 1
    return True

def choose_next_greedy(state, side):
    non_filled_count = 9 - np.count_nonzero(state)
    if non_filled_count == 0:
        return False
    index = 0
    list_states = []
    max_value_state = -1 
    for i in range(0,3):
        for j in range(0,3):
            if state[i, j] == 0:
                new_state = np.array(state)
                new_state[i, j] = side
                if value_map[str(new_state)] > max_value_state: 
                    max_value_state = value_map[str(new_state)]
                    list_states = [np.copy(new_state)]
                else if value_map[str(new_state)] == max_value_state:
                    list_states.append(np.copy(new_state))
                index = index + 1
    return True

state = np.matrix([[0,0,0], [0,0,0], [0,0,0]])

value_map = {}
value_map[str(state)] = 0.0

while True:
    if not choose_next(state, 1):
        break;
    print state
    if not choose_next(state, 2):
        break;
    print state
