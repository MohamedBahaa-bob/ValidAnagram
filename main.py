# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """if len(s) != len(t):
            return False
        else:
            for c in s:
                if c not in t:
                    return False
                t = t.replace(c, '', 1)
            return True"""
# better time complexity worse space complexity
        if len(s) != len(t):
            return False
        else:
            arr1 = []
            arr1.extend(s)
            arr2 = []
            arr2.extend(t)
            arr1.sort()
            arr2.sort()
            for i in range(0, len(arr1)):
                if arr1[i] != arr2[i]:
                    return False
            return True





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Solution()
    print(obj.isAnagram("anagram", "nagaram"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
