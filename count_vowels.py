def countVowels(user_input):
    vowels = "aeiou"
    count = 0
    for char in user_input.lower():
        if char in vowels:
            count += 1
    print(f"{user_input} has {count} vowels")

countVowels("AEIOU")
        