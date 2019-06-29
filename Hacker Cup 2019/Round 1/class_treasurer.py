
def main():

    T = int(input())

    for i in range(1, T+1):

        N, K = map(int, input().strip().split())
        classroom = input().strip()

        advantage = 0
        totalCost = 0

        # iterate through students backwards
        for index, student in enumerate(reversed(classroom)):

            # update advantage
            if student == 'B':
                advantage += 1
            elif advantage > 0:
                advantage -= 1
            
            # if advantage too high, bribe student
            if advantage > K:
                studentCost = 1
                for power in range(N - index):
                    studentCost = (studentCost * 2) % 1000000007

                totalCost = (totalCost + studentCost) % 1000000007
                advantage = max(0, advantage - 2)
            
        # print
        print("Case #" + str(i) + ": " + str(totalCost))


if __name__ == "__main__":
    main()
