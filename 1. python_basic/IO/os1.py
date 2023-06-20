import os

# -------------------------폴더 생성-------------------------
current_dir = os.getcwd() # cwd :  current working directory
print('현재 작업 폴더(디렉토리) : ',current_dir)

new_dir = "sesac_1234" # 새 디렉토리 만드는 과정
# os.mkdir(new_dir) # mk = make, dir = directory

def mkdirectory():
    for i in range(0, 10):
        dir_name = "sesac_"+str(i)
        os.mkdir(dir_name)

# mkdirectory()

# -------------------------폴더 삭제-------------------------
# rmdir(경로, *, dir_fd=없음)
# 디렉터리 경로를 제거(삭제)합니다. 디렉토리가 존재하지 않거나 비어 있지 않으면 각각 FileNotFoundError 또는 OSError가 발생합니다. 전체 디렉토리 트리를 제거하기 위해 shutil.rmtree()를 사용할 수 있습니다.
# 이 정도면 가까운 거리에 상대적인 경로를 연결할 수 있습니다.
# 버전 3.3에 추가: dir_fd 밀가루
# 버전 3.6에서 변경:순환형 객체를 가져옵니다.

dir_name = "sesac"
# os.mkdir(dir_name)
def remove_directory(dir_name):
    os.rmdir(dir_name)
#remove_directory(dir_name)


# -------------------------윈도우 내의 PYTHON 환경변수 출력-------------------------
python_path = os.getenv("PATH")
print(f"윈도우 내의 PYTHONPATH 환경변수 출력 : \n{python_path}")


# ----------------------------------컴퓨터 명령어 실행---------------------------------
# 서브 셸에서 명령(문자열)을 실행합니다. 이것은 표준 C 함수 system()를 호출하여 구현되며, 같은 제한이 있습니다. 
# sys.stdin 등의 변경 사항은 실행된 명령의 환경에 반영되지 않습니다. 
# command가 출력을 생성하면, 인터프리터 표준 출력 스트림으로 전송됩니다.
os.system("dir") # 디렉토리

my_command = ["explorer", "calc", "C:\Program Files\Google\Chrome\Application\chrome.exe"] 
for com in my_command:
    os.system(com)

