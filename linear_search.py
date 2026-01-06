class Linersearching:

    def solution(self, arr, element):

        i = 0

        ispresent = False

        while(i < len(arr)):

            if arr[i] == element:

                ispresent = True

                break

            i += 1

        print(ispresent)


lst = [10, 20, 30, 40, 50]

element = 20

linerinstance = Linersearching()

linerinstance.solution(lst, element)