# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            for c in s:
                if c not in t:
                    return False
                t = t.replace(c, '', 1)
            return True
            #if len(t) == 0:
            #    return True
            #else:
            #    return False




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.isAnagram("anagram", "nagaram"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
