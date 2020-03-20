import bencode

with open('sample.torrent', 'rb') as f:
    res = bencode.decode(f.read())

    for k in res:
        print(k)

    for f in res['info']['files']:
        print(f)
