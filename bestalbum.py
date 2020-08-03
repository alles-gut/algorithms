## programers.co.kr
## Hash - 베스트 앨범

def solution(genres, plays):
    album = []
    genrelist = {}
    order = []
    countgenre = 0
    for song_id in range(len(plays)):
        if genres[song_id] not in genrelist:
            genrelist[genres[song_id]] = [plays[song_id], song_id, plays[song_id]]
            countgenre += 1
        elif len(genres[song_id]) == 3:
            genrelist[genres[song_id]][0] += plays[song_id]
            genrelist[genres[song_id]].append(song_id)
            genrelist[genres[song_id]].append(plays[song_id])
        else:
            genrelist[genres[song_id]][0] += plays[song_id]
            if plays[song_id] > genrelist[genres[song_id]][2]:
                genrelist[genres[song_id]][1] = song_id
                genrelist[genres[song_id]][2] = plays[song_id]
            elif plays[song_id] == genrelist[genres[song_id]][2] or plays[song_id] > genrelist[genres[song_id]][4]:
                genrelist[genres[song_id]][3] = song_id
                genrelist[genres[song_id]][4] = plays[song_id]

        if countgenre == 0:
            order.append(countgenre)
        else:
            point = list(genrelist.keys()).index(genres[song_id])
            order.remove(point)
            for ind, genreid in order:
                if genrelist[list(genrelist.keys())[genreid]][0] < genrelist[list(genrelist.keys())[point]][0]:
                    order.insert(ind, point)
                    break
    for genreid in order:
        album.append(genrelist[list(genrelist.keys())[genreid]][1])
        album.append(genrelist[list(genrelist.keys())[genreid]][3])
    return album
