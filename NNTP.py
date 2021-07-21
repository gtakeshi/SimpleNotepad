from nntplib import NNTP
server =  NNTP("news.eternal-september.org")
group = "comp.lang.python.announce"
# server.group("comp.lang.python.announce")[0]
howmany = 10

resp,count,first,last,name = server.group(group)

start = last - howmany+1

resp,overviews = server.over((start,last))

for id ,over in overviews:
    subject = over["subject"]
    resp, info = server.body(id)
    print(subject)
    print("-" * len(subject))
    for line in info.lines:
        print(line.decode("latin1"))
    print()

server.quit()