from sys import argv


class Solutions:
    def andrii_burka(self, user_input):
        #   This solutions is 100/100 in OJS;    Author: Andrii Burka;
        user_input = reversed(input().split("|"))
        matrix = [li.split() for li in user_input]
        print(" ".join(num for li in matrix for num in li))

    def icakad(self):
        #   This solutions is only 75/100 in OJS;
        matrix = input().split('|')
        matrix = [[x for x in item.split(' ') if len(x) and x.isdigit()] for item in matrix]
        print(' '.join([' '.join(rr) for rr in reversed(matrix)]))

print(len(argv))