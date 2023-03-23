# pip list: 파이썬 공용공간에 설치된 모든 패키지 목록 확인
# 패키지명, 패키지 버전이 알파벳 순서로 출력

# python -m venv 가상환경이름
 # > 가상환경 만들기
 # > -m은 module name을 의미해서 venv라는 모듈을 쓰겠다는 의미

# python -m venv myenv 입력 시 폴더 생성됨

# .\myenv\Scripts\activate << 가상환경 들어가짐
# 직접 폴더에서 들어가도 됨

# 가상환경에서 pip list 써보면 상당히 패키지가 적다.
# pip install xlwings << 가상환경에서 입력

# ctrl+shift+p 후 python select interpreter 또는
# 우측 아래 파란색에 python 써진 부분
# 클릭 후 가상환경 선택

# pip freeze를 통해 현재 환경에 설치된 모든 패키지, 버전정보를 나타내준다.
# 이걸 그대로 복사해서 txt로 만들어도 되고
# pip freeze > 파일명(requirements.txt) 치면 텍스트 파일로 만들어준다.

# deactivate 입력하여 가상환경 빠져나오기 (터미널)
# vscode에서도 따로 벗어나주면 된다

# 가상환경 필요없어지면 rmdir 파일명 입력해서 삭제하면된다.
# 직접 지워도 된다. (myenv 폴더)

# python -m venv myenv --system-site-packages
 # > 이렇게 생성하고 pip list 하면 기존 공용으로 만들어둔 패키지 포함된다
 # > 이후 생성한 부분이 가상 로컬 환경에 설치된다.

# pip list --local
 # > 요렇게 list를 보면 가상환경에 설치된 패키지만 보인다

# 각 프로젝트별 필요로 하는 패키지 및 패키지버전이 다를 수 있으므로
# 가급적 새 프로젝트만들 때는 가상환경 만들어서 하는 것을 권해드립니다.






import xlwings

print(xlwings.__version__)
