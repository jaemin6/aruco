import cv2
import cv2.aruco as aruco
import numpy as np
import os

# --- 설정 변수 (변경할 부분) ---
# 사용할 Aruco 딕셔너리 정의 (예: 5x5 크기에 1000개의 고유 ID를 가진 딕셔너리로 변경)
# Aruco 공식 문서를 참고하여 프로젝트에 맞는 딕셔너리를 선택할 수 있습니다.
ARUCO_DICT = aruco.DICT_5X5_1000 # 👈 딕셔너리 변경 예시

# 생성할 마커의 고유 ID (선택한 딕셔너리 범위 내에서 선택해야 합니다. 예: 5x5_1000은 0~999)
MARKER_ID = 42 # 👈 마커 ID 변경 예시

# 생성될 이미지의 픽셀 크기 (더 큰 크기로 변경)
MARKER_SIZE_PIXELS = 1000 # 👈 마커 크기 변경 예시

# 저장 경로 (필요하다면 변경 가능)
OUTPUT_DIR = "markers"

# --- 코드 실행 ---
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# 1. 딕셔너리 로드
aruco_dict = aruco.getPredefinedDictionary(ARUCO_DICT)

# 2. 마커 이미지 생성 (흰색 배경에 검은색 패턴)
marker_image = aruco.generateImageMarker(aruco_dict, MARKER_ID, MARKER_SIZE_PIXELS)

# 3. 이미지 저장
file_name = os.path.join(OUTPUT_DIR, f"aruco_id_{MARKER_ID}_{MARKER_SIZE_PIXELS}px.png")
cv2.imwrite(file_name, marker_image)

print(f"✅ Aruco 마커 (ID: {MARKER_ID})가 '{file_name}'로 저장되었습니다.")