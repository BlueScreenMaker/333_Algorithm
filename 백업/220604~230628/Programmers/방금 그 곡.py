def change_melody(mel):
    mel=mel.replace('A#','a').replace('F#','f').replace('C#','c').replace('D#','d').replace('E#','e').replace('G#','g')
    return mel


def solution(m, musicinfos):
    m=change_melody(m)
    song=[]
    global flag
    flag=False
    global answer
    global me
    me=0
    answer = ''
    for i in range(len(musicinfos)):
        start_time, end_time, name, melody=musicinfos[i].split(",")
        melody=change_melody(melody)
        start_hour, start_end=start_time.split(":")
        end_hour, end_end=end_time.split(":")
        total_time=(int(end_hour)-int(start_hour))*60+(int(end_end)-int(start_end))
        sing=melody*(total_time//len(melody))+melody[0:total_time%len(melody)]
        song.append([sing,name])
    for j in range(0,len(song)):
        if m in song[j][0]:
            if not flag:
                flag=True
                me=j
            else:
                if(len(song[me][0])<len(song[j][0])):
                    me=j
    if not flag:
        answer='(None)'
    else:
        answer=song[me][1]
    return answer


print(solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))



''' 딕셔너리 이용 - KEY중복이 생기지 않을 거라는 조건이 문제에 없기 때문에 위험성이 있음
def change_melody(mel):
    mel=mel.replace('A#','a').replace('F#','f').replace('C#','c').replace('D#','d').replace('E#','e').replace('G#','g')
    return mel


def solution(m, musicinfos):
    m=change_melody(m)
    song={}
    global flag
    flag=False
    global answer
    global me
    me=''
    answer = ''
    for i in range(len(musicinfos)):
        start_time, end_time, name, melody=musicinfos[i].split(",")
        melody=change_melody(melody)
        start_hour, start_end=start_time.split(":")
        end_hour, end_end=end_time.split(":")
        total_time=(int(end_hour)-int(start_hour))*60+(int(end_end)-int(start_end))
        sing=melody*(total_time//len(melody))+melody[0:total_time%len(melody)]
        song[sing]=name
    for j in song.keys():
        if m in j:
            if not flag:
                me=j
                flag=True
            else:
                if len(j)>len(me):
                    me=j
    if not flag:
        answer='(None)'
    else:
        answer=song[me]
    return answer
'''