def solution(files):
    tmp = []
    head, number, tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit(): # 숫자가 나오면 그 이전은 무조건 HEAD, 그 이후는 NUMBER, TAIL
                head = file[:i]
                number = file[i:]

                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break

                tmp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    tmp = sorted(tmp, key=lambda x:(x[0].lower(), int(x[1])))

    return [''.join(i) for i in tmp]

solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])



# head, number, tail 로 분리하는게 중요
# 대소문자 비교 x
# tail 은 정렬 순서에 관여 x -> 들어온 순서대로 정렬이 유지되어야 함
# 01 과 1 은 같은 순서이다.

# 파이썬 sort 는 stable 정렬 -> 입력 순서 그대로 정렬 유지됨