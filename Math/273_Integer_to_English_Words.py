# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:54:32 2022

@author: Fan Luo
"""
"""
273. Integer to English Words

Convert a non-negative integer num to its English words representation.

Input: num = 123
Output: "One Hundred Twenty Three"
"""
class Solution:
    def numberToWords(self, num):
        def get_three_digit(num):
            if not num:
                return ""
            if not num // 100:
                return get_two_digit(num)
            return one_digit[num // 100] + " Hundred" + ((" " + get_two_digit(num % 100)) if num % 100 else "")
        def get_two_digit(num):
            if not num:
                return ""
            elif num < 10:
                return one_digit[num]
            elif num < 20:
                return two_digit[num]
            return tens[num // 10] + ((" " + one_digit[ num % 10 ]) if( num % 10 ) else "")
        
        one_digit = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }

        two_digit = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        tens = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        
        if(num == 0): return "Zero"
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        last_three = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        res = ''
        if billion:        
            res = get_three_digit(billion) + ' Billion'
        if million:
            res += ' ' if res else ''    
            res += get_three_digit(million) + ' Million'
        if thousand:
            res += ' ' if res else ''
            res += get_three_digit(thousand) + ' Thousand'
        if last_three:
            res += ' ' if res else ''
            res += get_three_digit(last_three)
        return res
