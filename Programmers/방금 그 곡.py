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


print(solution("ABCDEFG",	["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
