import queue,time
pq=queue.PriorityQueue()
new_coord=[]
def ascSort(list_tuple):
   for i in list_tuple:
    pq.put(i)
   for i in range(len(list_tuple)):
    new_coord.append(pq.get(i))
   return new_coord
# list_tuple=[(20, 18), (16, 26), (39, 45), (23, 35), (33, 43), (36, 13),
#            (11, 39), (43, 38), (21, 31), (62, 23), (42, 38), (31, 39), 
#            (65, 42), (60, 22), (29, 32), (40, 52), (30, 16), (17, 54), (54, 12), (57, 44)]


# x_min = min(p[0] for p in points)
# x_max = max(p[0] for p in points)
# y_min = min(p[1] for p in points)
# y_max = max(p[1] for p in points)

# dx = x_max - x_min
# dy = y_max - y_min
# delta_max = max(dx, dy)
# mid_x = (x_min + x_max) / 2
# mid_y = (y_min + y_max) / 2

# A = (mid_x - 20 * delta_max, mid_y - delta_max)
# B = (mid_x, mid_y + 20 * delta_max)
# C = (mid_x + 20 * delta_max, mid_y - delta_max)
