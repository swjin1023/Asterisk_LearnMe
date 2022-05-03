# selenium 모듈 import
from selenium import webdriver

# 크롬드라이버 경로 설정
chrome_driver_path = "크롬드라이버 설치 경로"

# 크롤링 옵션 생성
options = webdriver.ChromeOptions()
# 백그라운드 실행 옵션 추가
options.add_argument("headless")

# 크롬 드라이버 실행
driver = webdriver.Chrome(executable_path = chrome_driver_path, chrome_options= options)