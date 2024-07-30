calls = 0

def string_info(string):
    count_calls()
    info = (len(string), string.upper(), string.lower())
    return info

def is_contains(string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            return True
    return False
def count_calls():
    global calls
    calls = calls + 1

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)




