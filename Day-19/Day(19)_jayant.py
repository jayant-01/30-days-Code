def count_words(file_name):
    file = open(file_name)
    count = 0
    words = list(file.read().split(' '))
    for word in words:
        count += 1
    
    print('Number of words:', count)
def count_lines(file_name):
    file = open(file_name)
    count = 0
    lines= list(file.read().split('.'))
    for line in lines:
        count += 1
    print('Number of lines:', count-1)

count_words('obama_speech.txt')
count_lines('obama_speech.txt')

count_lines('michelle_obama.txt')
count_words('michelle_obama.txt')

count_lines(danald_speech.txt)
count_words(donald_speech.txt)

count_lines('melina_trump_speech.txt')
count_words('melina_trump_speech.txt')

f=open('email_exchange big.txt','r')
l=list(f.read().split(' '))
print(l)
