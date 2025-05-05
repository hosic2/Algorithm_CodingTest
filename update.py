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

        # 카테고리별 제목 및 표 생성
        if directory not in directories:
            if directory in ["백준", "프로그래머스"]:
                content += "## 📚 {}\n".format(directory)
            else:
                if directory in [0, 1, 2, 3, 4, 5, '0', '1', '2', '3', '4', '5']:
                    content += "### 🚀 Lv{}\n".format(directory)
                else:
                    content += "### 🚀 {}\n".format(directory)

            # 토글을 위한 details, summary 추가
            content += "<details>\n"
            content += "  <summary>문제 목록 보기</summary>\n"
            directories.append(directory)

            # 문제 목록을 표로 작성
            content += "| 문제번호 | 링크 |\n"
            content += "| ----- | ----- |\n"

        for file in files:
            if category not in solveds:
                problem_number = os.path.basename(file).split('.')[0]
                # 문제 번호와 링크 처리
                problem_link = parse.quote(os.path.join(root, file).replace("\\", "/"))
                content += "| {} | [문제 보러가기](./{}) |\n".format(problem_number, problem_link)
                solveds.append(category)

        # 토글 종료 태그
        content += "</details>\n"

    with open("README.md", "w") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
