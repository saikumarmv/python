pagram = "The quick brown for jumps over the lazy dog"
letter = sorted(pagram)
print(letter)
numbers = [1.2, 9.5, 6.3, 3.6, 5.4]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# case sensitive sorting
missing_letter = sorted("The Quick brow fox jumpeed ovwer the lazy dog",
                        key=str.casefold)
print(missing_letter)
name = ["Graham",
        "John",
        "terry",
        "eric",
        "terry",
        "Michel"]
name.sort(key=str.casefold)
print(name)