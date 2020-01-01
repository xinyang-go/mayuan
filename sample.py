import random

def create(fn, encoding="utf-8"):
    fp = open(fn, "r", encoding=encoding)
    lines = fp.readlines()
    probs = []
    curr = []
    for l in lines:
        s = l[0]
        if ord("0") <= ord(s) <= ord("9"):
            if curr:
                probs.append(curr)
            p = a = ""
            for c in l:
                if ord("A") <= ord(c) <= ord("E"):
                    a += c
                else:
                    p += c
            curr = [[p, a]]
        elif ord("A") <= ord(s) <= ord("E"):
            curr.append(l)
    return probs
    
def main():
    probs = create("base.txt")
    random.shuffle(probs)
    for p in probs:
        a = p[0][1]
        print(p[0][0])
        for n in p[1:]:
            print(n)
        input("回车查看答案")
        print("答案：", a)
        input("回车以继续...\n")
        
if __name__ == "__main__":
    main()