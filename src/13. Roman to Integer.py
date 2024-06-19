# https://leetcode.com/problems/roman-to-integer/description/ for question

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_nums = {
                        'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000,
                        'IV': 4,
                        'IX': 9,
                        'XL': 40,
                        'XC': 90,
                        'CD': 400,
                        'CM': 900
                    }

        integer_list = []
        counter = len(s)
        s_range = iter(range(len(s)))
        
        for i in s_range:
            if counter > 1:
                rom_val = ''.join([s[i],s[i+1]])
                if rom_val in list(rom_nums.keys()):
                    integer_list.append(rom_nums[rom_val])
                    i = next(s_range)
                    counter -= 2
                    continue
                else:
                    integer_list.append(rom_nums[s[i]])
                    counter -= 1
                    continue
            else:
                integer_list.append(rom_nums[s[i]])

        return sum(integer_list)