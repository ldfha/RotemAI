# 자동차가 이동하며 여러 방향으로 레이저를 쏘고 건물 표면 좌표를 수집하여
# 3D 점군(Point Clouds) 생성
# 라이다는 물체를 면으로 보는 것이 아니라, 많은 점좌표(x, y)를 모아 환경을 재구성한다.
# 즉, [x, y, z] 이런 점으로 구성할 수 있다.

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as Axes3D

# 도시 환경 정의 : 각 건물은 직육면체 형태 (xmin, xmax, ymin, ymax, zmin, zmax)
building = [
    (-20, 10, 10, 20, 0, 20),
    (10, 20, 15, 25, 0, 25),
    (-15, -5, 35, 45, 0, 18),
    (5, 18, 50, 60, 0, 30)
]
car_positions = []  # 자동차 이동 경로

# 자동차가 y축 방향으로 이동. y=0 ~ y=60 구간을 25개 위치로 나눔
for y in np.linspace(0, 60, 25):
    car_positions.append(np.array([0, y, 2]))   # 차량 위치, 현재 전진 위치, 센서 높이

# print('car positions :', car_positions)

# LiDAR 스캔 함수
def simulate_lidar(car_pos):
    pass

all_points = []

for pos in car_positions:
    scan_points = simulate_lidar(pos)
    all_points.extend(scan_points)