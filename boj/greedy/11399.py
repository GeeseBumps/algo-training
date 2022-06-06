from typing import List


def sol_1(n: str, times: List[str]) -> None:
    result = 0
    times = [int(t) for t in times]
    times.sort()
    for i in range(int(n)):
        result += (int(n)-i) * times[i]
    print(result)

if __name__=="__main__":
    n = input()
    times = input().split(' ')
    sol_1(n, times)
