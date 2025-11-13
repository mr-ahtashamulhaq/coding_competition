def solve(W1: str, W2: str) -> str:
    """
    Return the string containing the word you should say
 
    W1: the second-to-last word said 
    """
    def nTw(n):
        if n % 15 == 0:
            return "bizzfuzz"
        if n % 3 == 0:
            return "bizz"
        if n % 5 == 0:
            return "fuzz"
        return str(n)

    n2 = -1

    if W2.isdigit():
        n2 = int(W2)
        
    elif W1.isdigit():
        n1 = int(W1)
        n2 = n1 + 1
        
    else:
        possN2 = []
        for i in range(2, 102):
            if nTw(i) == W2 and nTw(i - 1) == W1:
                possN2.append(i)

        if len(possN2) == 1:
            n2 = possN2[0]
        else:
            return "crap"

    if n2 != -1:
        return nTw(n2 + 1)
    else:
        return "crap"

def main():
    T = int(input())
    for _ in range(T):
        W1 = input()
        W2 = input()
        print(solve(W1, W2))

if __name__ == '__main__':
    main()