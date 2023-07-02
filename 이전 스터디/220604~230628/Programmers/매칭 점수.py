import re


def solution(word, pages):
    web_page=[]
    web_name=[]
    web_group=dict() # 나를 가리키는 외부 링크

    for html in pages:
        # \s = 공백  내 링크 저장
        url=re.search('<meta property="og:url" content="(\S+)"', html).group(1)
        base_point=0
        # 알파벳으로 이루어진 단어만 골라내기 (특수문자 제거)
        for check in re.findall(r'[a-zA-Z]+', html.lower()):
            if check==word.lower():
                base_point+=1
        export_link = re.findall('<a href="(https://[\S]*)"', html)
        # https:// 뒤에 공백이 올 수 있어서 \s 표시, *은 문자가 0~N개 온다고 가정

        for link in export_link:
            if link not in web_group.keys():
                web_group[link] = [url]
            else:
                web_group[link].append(url)

        web_name.append(url)
        web_page.append([url, base_point, len(export_link)])

    max_value=0
    answer = 0
    for i in range(len(web_page)):
        values=web_page[i][0]
        total=web_page[i][1]

        if values in web_group.keys():
            for check in web_group[values]:
                u, b, c = web_page[web_name.index(check)]
                total += (b/c)

        if max_value < total:
            max_value=total
            answer=i
    return answer

print(solution("blind", ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
                         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
                         "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]))

#https://velog.io/@ckstn0778/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-42893%EB%B2%88-%EB%A7%A4%EC%B9%AD-%EC%A0%90%EC%88%98-X-1-Python