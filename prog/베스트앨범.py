def solution(genres, plays):
    answer = []
    
    # 장르별로 노래 정보를 딕셔너리에 저장
    song_dict = {}
    for i in range(len(genres)):
        genre = genres[i]
        play_count = plays[i]
        
        if genre not in song_dict:
            song_dict[genre] = []
        
        song_dict[genre].append((i, play_count))
    
    # 장르별 재생 횟수를 합산하여 정렬
    sorted_genres = sorted(song_dict.keys(), key=lambda x: sum(p[1] for p in song_dict[x]), reverse=True)
    sorted(song_dict.keys())
    # 각 장르별 두 개씩 노래 선택
    for genre in sorted_genres:
        songs = song_dict[genre]
        songs.sort(key=lambda x: (-x[1], x[0]))  # 재생 횟수 내림차순, 인덱스 오름차순 정렬
        
        for i in range(min(2, len(songs))):
            answer.append(songs[i][0])
    
    return answer