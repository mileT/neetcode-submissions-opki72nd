class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits or len(digits) == 0:
            return []
        # Create a dictionary mapping each digit to its corresponding letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        # Initialize a list to store the combinations   
        combinations = ['']
        # Iterate through each digit in the input string
        for digit in digits:
            # For each digit, generate new combinations by appending each letter to the existing combinations
            new_combinations = []
            for letter in digit_to_letters[digit]:
                for combination in combinations:
                    new_combinations.append(combination + letter)
            # Update the list of combinations with the new combinations
            combinations = new_combinations
        # Return the list of combinations
        return combinations
        