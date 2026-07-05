import sys
from collections import defaultdict

def processGame(events, H):
    """
    events: list of tuples (player, frame, attack_value)
        player: 1 or 2
        frame: non-negative integer
        attack_value: positive integer
    H: starting HP for both players

    Returns: [hp1, hp2] with each clamped to min 0
    """
    # TODO: Implement the corrected game logic
    # Hint: Group events by frame, process each frame atomically
    
    h1 = H
    h2 = H

    events.sort(key=lambda x: x[1])

    grp = defaultdict(list)
    for p, f, a in events:
        grp[f].append((p, a))

    for f in sorted(grp.keys()):
        d1 = 0
        d2 = 0

        for p, a in grp[f]:
            if p == 1:
                d2 += a
            else:
                d1 += a

        h1 -= d1
        h2 -= d2

        h1 = max(0, h1)
        h2 = max(0, h2)

        if h1 == 0 or h2 == 0:
            break

    return [h1, h2]


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        H = int(input().strip())
        n = int(input().strip())
        events = []
        for _ in range(n):
            parts = input().strip().split()
            events.append((int(parts[0]), int(parts[1]), int(parts[2])))

        result = processGame(events, H)
        print(f"{result[0]} {result[1]}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)



