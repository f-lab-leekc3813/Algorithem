def solution(s, n):
    result = ''
    for char in s:
        if char.isalpha():
            code = ord(char)
            new_code = code + n
            if char.islower():
                if new_code > ord('z'):
                    new_code -= 26
                elif new_code < ord('a'):
                    new_code += 26
            else:
                if new_code > ord('Z'):
                    new_code -= 26
                elif new_code < ord('A'):
                    new_code += 26
            result += chr(new_code)
        else:
            result += char
                    
    return result