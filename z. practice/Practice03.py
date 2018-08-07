def splitDirectory(s):
    result = s.rsplit("/", 1)

    return result

def splitAll(s):
    results = s.replace("/", " ").strip().split(" ")

    return results

def printAll(lists):
    results = []
    for sub in lists:
        sub = "'" + sub + "'"
        results.append(sub)

    for i in range(0,len(results)):
        if i < len(results)-1:
            print(results[i], end=", ")
        else:
            print(results[i])


s = '/usr/local/bin/python'

printAll(splitAll(s))
printAll(splitDirectory(s))
