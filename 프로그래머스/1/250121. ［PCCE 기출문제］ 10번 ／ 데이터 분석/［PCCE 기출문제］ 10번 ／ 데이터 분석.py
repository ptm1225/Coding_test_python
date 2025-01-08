def solution(data, ext, val_ext, sort_by):
    d = ['code', 'date', 'maximum', 'remain']
    data = [x for x in data if x[d.index(ext)] < val_ext]
    return sorted(data, key=lambda x: x[d.index(sort_by)])