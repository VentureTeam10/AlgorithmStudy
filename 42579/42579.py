#베스트엘범
def solution(genres, plays):
    answer = []
    count = {}
    song = {}
    
#장르별 재생횟수 계산, 노래 데이터 리스트 생성
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in count:
            count[genre] = play
        else:
            count[genre] += play

        if genre not in song:
            song[genre] = [(i, play)]
        else:
            song[genre].append((i, play))

#재생 횟수 높은 순으로 정렬
    sorted_genres = sorted(count.keys(), key=lambda x: count[x], reverse=True)

#각 장르별 최대 2개 선택    
    for genre in sorted_genres:
        pickup = song[genre]
        pickup = sorted(pickup, key=lambda x: (-x[1], x[0]))
        for i in range(min(len(pickup), 2)):
            answer.append(pickup[i][0])

    return answer
