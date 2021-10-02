#Solution for leet code problem Counting bits https://leetcode.com/problems/counting-bits/
class Solution:
    def countBitsOfNumber(self, number: int , list_item):
        number_of_bits= 0
        if(number == 1):
            list_item[number] = 1
            
        if(list_item[number] != -1):
            number_of_bits = list_item[number]
        else:
            
            if(number % 2 == 0):
                number_of_bits = self.countBitsOfNumber(number//2,list_item)
                list_item[number] = number_of_bits
            else:
                number_of_bits = self.countBitsOfNumber((number-1)//2,list_item) + 1
                list_item[number] = number_of_bits
        #print ("number = {} number_of_bits = {}".format(number,number_of_bits))
        return number_of_bits
        
    def countBits(self, n: int) -> List[int]:
        ret = [-1] * (n+1)
        ret[0] = 0
       
        for i in range(n+1):
            self.countBitsOfNumber(i,ret)
        return ret
