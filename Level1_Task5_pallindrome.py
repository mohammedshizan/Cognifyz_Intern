def is_palindrome(sequence):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    sequence = sequence.replace(" ", "").lower()
    # Check if the sequence is equal to its reverse
    return sequence == sequence[::-1]

# Input sequence from the user
user_input = input("Enter a sequence: ")

if is_palindrome(user_input):
    print("The sequence is a palindrome.")
else:
    print("The sequence is not a palindrome.")
