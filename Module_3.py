calls = 0
def count_calls ():
    global calls
    calls = 25 * 5
def string_info (string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains (string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

print(string_info('Urban'))
print(string_info('Python'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('goodbye', ['good afternoon', 'how is your mood']))
print(calls)