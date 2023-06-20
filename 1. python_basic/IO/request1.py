import requests # https://pypi.org/project/requests/
# 그렇다면, 웹 페이지도 가져올 수 있을까?
# 크롬을 띄우고 마우스를 이동해서 주소창을 치고 그 결과를 복사하고...
# 일반적으로 웹에 있는 컨텐츠를 가져오기 위해서 GUI 사람이 하는 행위 반복할 필요 X
# 코드를 통해서 정보(contents)를 가져오고 싶음...

# 추가 패키지 설치 : pip(Preferred Installer Packages) install / conda install

# pip install requests 할 때는 환경 확인이 필수. py38_62_sesac엔 설치해도 다른 환경에서 다시 사용하려면 설치 필수
# 기본적으로 최신 버전이 설치되며, 특정 버전을 설치하고 싶으면 pip install requests==2.0.0 으로
# 존재하는 것 설치 시, 과거 설치된 버전이 삭제되고 최신 명령의 버전이 설치됨



# ---------------네이버 페이지의 내용을 받아와서 화면에 텍스트로 출력하시오---------------
# request.get(url).status_code : 응답상태 
# request.get(url).text : 페이지 내용 텍스트 
response = requests.get('https://www.naver.com')
# 네이버 페이지 내에서 가져온 컨텐츠 내에서 <H2> 라는 태그로 작성된 컨텐츠를 찾아서 출력
contents = response.text
search_str = "<link"
# 순회
for line in contents.splitlines(): 
    if search_str in line:
        print(line.strip()) #strip() : 공백 제거