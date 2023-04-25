if __name__ == '__main__':
    leaderboard = []
    name_we_need = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        name_score = [score, name]
        leaderboard.append(name_score)
        leaderboard.sort()
        print(leaderboard)
        print(len(leaderboard))

    for i in range(len(leaderboard)):
        if i + 1 == len(leaderboard):
            break
        if leaderboard[i][0] < leaderboard[i + 1][0]:
            name_we_need.append(leaderboard[i + 1][1])
            print(name_we_need)
            if leaderboard[i + 1][0] == leaderboard[i + 2][0]:
                name_we_need.append(leaderboard[i + 2][1])
                print(name_we_need)
                break

    name_we_need.sort()
    print(name_we_need)

    # for i in name_we_need:
    #     print(i)