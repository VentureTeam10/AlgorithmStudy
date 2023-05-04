def solution(genres, plays):

    genre_sum = dict()
    songs_idx = dict()
    answer = []

    for i in range(len(genres)):
        if genres[i] in genre_sum:
            genre_sum[genres[i]] += plays[i]
            songs_idx[genres[i]][i] = plays[i]
        else:
            genre_sum[genres[i]] = plays[i]
            songs_idx[genres[i]] = {i: plays[i]}

    genre_sum = dict(sorted(genre_sum.items(), key=lambda x: x[1], reverse=True))

    for genre in genre_sum:
        songs_idx[genre] = dict(sorted(songs_idx[genre].items(), key=lambda x: x[1], reverse = True))
        idx = list(songs_idx[genre].keys())
        answer.extend(idx[:2])

    return answer