import sys
import random

def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # WRITE YOUR CODE HERE
    
    # Initialize 10x10 grid with empty spaces
    grid = [[' ' for _ in range(10)] for _ in range(10)]
    
    # Clean and prepare words (convert to uppercase, remove invalid words)
    clean_words = []
    for word in words:
        word = word.upper().strip()
        if word and len(word) <= 10 and word.isalpha():
            clean_words.append(word)
    
    # Sort words by length (longest first) for better placement success
    clean_words.sort(key=len, reverse=True)
    
    # Direction vectors: [row_delta, col_delta] for 8 directions
    directions = [
        (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1)   # Diagonal up-right
    ]
    
    def can_place_word(word, start_row, start_col, direction):
        """Check if a word can be placed at given position and direction"""
        dr, dc = direction
        
        for i, char in enumerate(word):
            r = start_row + i * dr
            c = start_col + i * dc
            
            # Check bounds
            if r < 0 or r >= 10 or c < 0 or c >= 10:
                return False
                
            # Check if position is empty or has matching character
            if grid[r][c] != ' ' and grid[r][c] != char:
                return False
                
        return True
    
    def place_word(word, start_row, start_col, direction):
        """Place a word in the grid at given position and direction"""
        dr, dc = direction
        
        for i, char in enumerate(word):
            r = start_row + i * dr
            c = start_col + i * dc
            grid[r][c] = char
    
    def get_valid_positions(word):
        """Get all valid positions where a word can be placed"""
        valid_positions = []
        
        for direction in directions:
            dr, dc = direction
            
            # Calculate valid starting positions for this direction
            for row in range(10):
                for col in range(10):
                    # Check if word would fit within bounds
                    end_row = row + (len(word) - 1) * dr
                    end_col = col + (len(word) - 1) * dc
                    
                    if 0 <= end_row < 10 and 0 <= end_col < 10:
                        if can_place_word(word, row, col, direction):
                            valid_positions.append((row, col, direction))
        
        return valid_positions
    
    # Place each word in the grid
    placed_words = []
    
    for word in clean_words:
        valid_positions = get_valid_positions(word)
        
        if valid_positions:
            # Randomly select from valid positions for variety
            position = random.choice(valid_positions)
            start_row, start_col, direction = position
            place_word(word, start_row, start_col, direction)
            placed_words.append(word)
        
        # If word couldn't be placed, try a few more times with current state
        elif len(placed_words) < len(clean_words):
            attempts = 0
            while attempts < 10:  # Try up to 10 times
                valid_positions = get_valid_positions(word)
                if valid_positions:
                    position = random.choice(valid_positions)
                    start_row, start_col, direction = position
                    place_word(word, start_row, start_col, direction)
                    placed_words.append(word)
                    break
                attempts += 1
    
    # Fill empty spaces with random letters
    # Use frequency-based letter selection for more realistic appearance
    letter_weights = {
        'A': 8, 'B': 2, 'C': 3, 'D': 4, 'E': 12, 'F': 2, 'G': 2, 'H': 6,
        'I': 7, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 7, 'O': 8, 'P': 2,
        'Q': 1, 'R': 6, 'S': 6, 'T': 9, 'U': 3, 'V': 1, 'W': 2, 'X': 1,
        'Y': 2, 'Z': 1
    }
    
    letters = []
    for letter, weight in letter_weights.items():
        letters.extend([letter] * weight)
    
    # Fill remaining empty spaces
    for i in range(10):
        for j in range(10):
            if grid[i][j] == ' ':
                grid[i][j] = random.choice(letters)
    
    return grid


# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = create_crossword(words)
        
        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)