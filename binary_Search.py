class Binarysearch:

    def solution(self, arr, element):

        arr.sort()

        low = 0

        upp = len(arr) - 1

        ispresent = False

        while(low <= upp):

            mid = (low + upp) // 2

            if element == arr[mid]:

                ispresent = True

                break

            elif element < arr[mid]:

                upp = mid - 1

            elif element > arr[mid]:

                low = mid + 1

        print(ispresent)

binaryinstance = Binarysearch()

binaryinstance.solution([10, 20, 30, 40, 50, 60, 70], 100)



