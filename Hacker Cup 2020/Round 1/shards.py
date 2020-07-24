
def main():


    inf = open('new_in.txt', 'r')
    out_file = open('shards_out.txt', 'w')

    # no. airlines
    T = int(next(inf))
    for i in range(1, T+1):

        # get inputs
        N = int(next(inf))
        C = next(inf).strip()
        ans = 'N'
        if abs(C.count('A') - C.count('B')) < 2:
            ans = 'Y'

        # print
        print("Case #" + str(i) + ": " + ans + "\n")
        out_file.write("Case #" + str(i) + ": " + ans + "\n")


if __name__ == "__main__":
    main()
