def solution(phone_book):
    phone_book.sort() 

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False 

    return True  


def solution(phone_book):
    answer = True
    phone_book.sort()
    if len(phone_book) >1:
        for i in range(len(phone_book)-1):
            a = phone_book[i]
            if a == phone_book[i+1][:len(a)]:
                answer = False
    else:
         answer = True   
    return answer


# 다른사람 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer