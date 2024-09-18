There are a few ways to optimize this code:

1. **Use functions more effectively**:
   - The `standing()` function is doing too many things. It should only display the current state of the game.
   - Create separate functions for checking game-ending conditions, determining the winner, and handling the computer's turn.
   - This will make the code more modular, readable, and easier to maintain.

2. **Use more descriptive variable names**:
   - Variable names like `player_hand`, `computer_hand`, `player_score`, and `computer_score` are clear, but others like `participant_hand` and `winner` could be more descriptive.

3. **Optimize the `calculate_score()` function**:
   - Instead of iterating over the entire list to find and replace 11s with 1s, you can use a more efficient approach:
     - First, count the number of 11s in the hand.
     - Then, replace 11s with 1s only if the score exceeds 21 and there are still 11s remaining.
     - This will save unnecessary iterations over the list.

4. **Use type hints consistently**:
   - While some functions have type hints, others don't. It's a good practice to use type hints consistently throughout the code for better readability and maintainability.

5. **Consider using classes**:
   - The game logic could be encapsulated in a `Blackjack` class, making the code more object-oriented and easier to extend or modify in the future.
   - For example, you could have separate classes for `Player`, `Dealer`, and `Card`.

6. **Separate game logic from user interface**:
   - Currently, the game logic and user interface (input/output) are intertwined.
   - Consider separating the game logic from the user interface to make the code more modular and easier to test and maintain.

7. **Improve error handling**:
   - The code currently doesn't handle invalid user inputs or other potential errors very well.
   - Add proper error handling and validation to make the code more robust.

8. **Consider using docstrings or comments more**:
   - While some functions have docstrings, others don't. Add docstrings or comments to improve code documentation and make it easier to understand for other developers (or your future self).

9. **Use Python's built-in functions effectively**:
   - For example, you could use `random.sample()` instead of `randint()` to choose random cards from the deck without replacement.

10. **Consider using external libraries**:
    - There are Python libraries specifically designed for playing card games, such as `pydealer`. Using such libraries can simplify the code and provide more features and flexibility.

Overall, while the code works as intended, there is room for improvement in terms of readability, maintainability, and extensibility.