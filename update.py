#!/usr/bin/env python

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
                content += "<details>\n"  # 시작: 토글 기능
                content += "<summary>문제 목록 보기</summary>\n"  # 요약 텍스트
                content += "\n"  # 요약과 문제 목록 사이의 빈 줄
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
                content += "| {} | [문제 보러가기]({}) |\n".format(category, parse.quote(os.path.join(root, file)))
                solveds.append(category)
                print("category : " + category)

        # 토글 기능 종료
        if directory in ["백준", "프로그래머스"]:
            content += "</details>\n"  # 종료: 토글 기능

    with open("README.md", "w") as fd:
        fd.write(content)
        
if __name__ == "__main__":
    main()
