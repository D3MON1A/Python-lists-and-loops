parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot():
  state = {
    'total_slots': 0,
    'available_slots': 0,
    'occupied_slots': 0
  }
  for x in range(len(parking_state)):
    for i in parking_state[x]:
      if i == 2:
        state['available_slots'] += 1
        state['total_slots'] += 1
      elif i == 1:
        state['occupied_slots'] += 1
        state['total_slots'] += 1
  return state
print(get_parking_lot())

# def get_parking_lot(): 
#     total_slots = []
#     available_slots = []
#     occupied_slots = []
#     for slots in parking_state:
#         for status in slots:
#             print(status)
#             # print(type(status))
#             if status == 1:
#                 occupied_slots =+ 1
#         # print(status)
#     print("Now the occupied slots")
#     print(occupied_slots)

# get_parking_lot()

#def get_parking_lot():
    #totalSlots = []
    #availableSlots = []
    #occupiedSlots = []
    #state=totalSlots, availableSlots, occupiedSlots

    # for slots in parking_state:
    #     for status in slots:
    #         if status == 0:
    #             status.append(availableSlots)
    #         elif status > 0:
#                 status.append(occupiedSlots)
#             else:
#                 status.append(totalSlots=+1)

#     print(state)

# get_parking_lot()



