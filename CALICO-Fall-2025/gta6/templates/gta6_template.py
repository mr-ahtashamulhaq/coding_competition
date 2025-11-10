def solve(E: str, Y: int, M: int, D: int) -> str:
    """

    E: The name of the event
    Y: Year
    M: Month
    D: Day
    """
    # YOUR CODE HERE
    gtaYear = 2026
    gtamon = 11
    gtaDay = 19
    
    if Y < gtaYear:
        return f"we got {E} before gta6"
    elif Y > gtaYear:
        return f"we got gta6 before {E}"
    else:
        if M < gtamon:
            return f"we got {E} before gta6"
        elif M > gtamon:
            return f"we got gta6 before {E}"
        else:
            if D < gtaDay:
                return f"we got {E} before gta6"
            elif D > gtaDay:
                return f"we got gta6 before {E}"
            else:
                return f"we got {E} before gta6"

def main():
    T = int(input())
    for _ in range(T):
        E = input()
        temp = input().split()
        Y, M, D = int(temp[0]), int(temp[1]), int(temp[2])
        print(solve(E, Y, M, D))

if __name__ == '__main__':
    main()