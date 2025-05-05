import os
from urllib import parse

HEADER = """# 
# 백준 & 프로그래머스 문제 풀이 목록
"""

def main():
    content = ""
    content += HEADER
    
    directories = []
    solveds = []

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        
        if category == 'images':
            continue
        
        directory = os.path.basename(os.path.dirname(root))
        
        if directory == '.':
            continue
            
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "## 📚 {}\n".format(directory)
            else:
                if directory in [0, 1, 2, 3, 4, 5, '0', '1', '2', '3', '4', '5']:
                    content += "### 🚀 Lv{}\n".format(directory)
                else:
                    content += "### 🚀 {}\n".format(directory)
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        for file in files:
            if category not in solveds:
                # 문제 번호 폴더 경로
                problem_folder = os.path.join(root, category)
                
                # 문제 폴더가 존재하지 않으면 생성
                if not os.path.exists(problem_folder):
                    os.makedirs(problem_folder)
                
                # 풀이가 2번째부터는 하위 폴더를 생성
                solution_index = len([name for name in os.listdir(problem_folder) if os.path.isdir(os.path.join(problem_folder, name))]) + 1
                solution_folder = os.path.join(problem_folder, f"풀이{solution_index}")
                
                # 풀이 하위 폴더가 없으면 생성
                if not os.path.exists(solution_folder):
                    os.makedirs(solution_folder)

                # 파일 경로 생성
                file_path = os.path.join(solution_folder, file)
                content += "|{}|[문제 보러가기]({})|\n".format(category, parse.quote(file_path))
                solveds.append(category)
                print("category : " + category)

    with open("README.md", "w") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
