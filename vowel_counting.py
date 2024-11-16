'''
In Python, you can create a function that counts the number of vowels in a given word. Vowels are the letters A, E, I, O, and U, both uppercase and lowercase. The function takes a single word as its parameter and returns the number of vowels present in the word.
To achieve this, you can use a for loop to iterate through each character in the word. Then, you can check if the character is a vowel using a conditional statement. If the character is a vowel, you add a counter variable. Then the counter variable is your final result.
'''

def count_vowels(word):
    word = word.lower()
    characters = list(word)
    vowel_count = 0
    vowels = ["a","e","i","o","u"]
    for letter in characters:
        for i in vowels:
            if i == letter:
                vowel_count += 1
    return vowel_count


def main():
    print(count_vowels("Education"))
    
main()
