parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot():
    totalSlots = []
    availableSlots = []
    occupiedSlots = []
    state={totalSlots, availableSlots, occupiedSlots}

    for slots in parking_state:
        for status in slots:
            if status == 0:
                status.append(availableSlots)
            elif status > 0:
                status.append(occupiedSlots)
            else:
                status.append(totalSlots=+1)

    print(state)

get_parking_lot()



