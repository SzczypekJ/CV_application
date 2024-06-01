class Solution:
    def numIslands(self, grid):
        dict_of_indexes = {}
        for index1, value1 in enumerate(grid):
            for index2, element in enumerate(value1):
                if element == '1':
                    dict_of_indexes[f"{index1}, {index2}"] = [element]

        # print(dict_of_indexes)
        for key, value in dict_of_indexes.items():
            print(key)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
sol = Solution()
print(sol.numIslands(grid))
