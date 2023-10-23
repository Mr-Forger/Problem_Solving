import math
import random


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair(points):
    if len(points) <= 3:
        min_dist = float('inf')
        closest_points = None
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                if distance(points[i], points[j]) < min_dist:
                    min_dist = distance(points[i], points[j])
                    closest_points = (points[i], points[j])
        return min_dist, closest_points

    mid = len(points) // 2
    mid_point = points[mid]

    dl, pair_l = closest_pair(points[:mid])
    dr, pair_r = closest_pair(points[mid:])

    if dl < dr:
        d = dl
        min_pair = pair_l
    else:
        d = dr
        min_pair = pair_r

    strip = [point for point in points if abs(point[0] - mid_point[0]) < d]
    strip.sort(key=lambda point: point[1])

    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < d:
            if distance(strip[i], strip[j]) < d:
                d = distance(strip[i], strip[j])
                min_pair = (strip[i], strip[j])
            j += 1

    return d, min_pair


# 코드 시작
N = 100
a = []
random.seed(0)
i = 0

while i < N:
    x_coord = random.randint(0, 2000)
    y_coord = random.randint(0, 1000)
    if [x_coord, y_coord] not in a:
        a.append([x_coord, y_coord])
        i += 1

print(a)
a.sort()  # x좌표에 따라 정렬
print(a)

# 가장 가까운 두 점 및 그 거리 출력
distance, points = closest_pair(a)
print(f"가장 가까운 두 점: {points}, 거리: {distance}")
