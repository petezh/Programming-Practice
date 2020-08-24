
def main():

    # no. airlines
    T = int(input())

    out_file = open('airlines_out.txt', 'w')

    for i in range(1, T+1):

        # get inputs
        N = int(input())
        I = input().strip()
        O = input().strip()
        P = []

        # find links
        countdown, countup = [False] * (N-1), [False] * (N-1)
        for j in range(0, N-1):
            countdown[j] = (I[j] == 'Y') and (O[j+1] == 'Y')
        for j in range(0, N-1):
            countup[j] = (I[j+1] == 'Y') and (O[j] == 'Y')
        print(countup)
        print(countdown)
        for n in range(0, N):
            # default
            p = ""
            #count up
            broken = False
            for j in reversed(range(0, n)):
                if not countdown[j] or broken:
                    p = 'N' + p
                    broken = True
                else:
                    p = 'Y' + p
            broken = False
            p += 'Y'
            for j in range(n+1, N):
                if not countup[j-1] or broken:
                    p += "N"
                    broken = True
                else:
                    p += 'Y'
            
            p += "\n"
            
            P += [p]
            
        # print
        out_file.write("Case #" + str(i) + ":\n") 
        for p in P:
            out_file.write(p)


if __name__ == "__main__":
    main()
