def most_trending(str,k):
    str = str.split(" ")
    out = {}
    for i in str:
        if i not in out.keys():
            out[i] = 1
        else:
            out[i] += 1

    out = dict(sorted(out.items(),reverse = True,key=lambda item : item[1]))

    for i in list(out.keys())[:k]:
        print(i,out[i])


str= "Welcome to the world of Geeks This portal has been created to provide well written well thought and well explained solutions for selected questions If you like Geeks for Geeks and would like to contribute here is your chance You can write article and mail your article to contribute at geeksforgeeks org See your article appearing on the Geeks for Geeks main page and help thousands of other Geeks"
k = 6
most_trending(str,k)