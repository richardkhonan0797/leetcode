class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last_row = self.getRow(rowIndex - 1)
        res = [1]
        for i in range(len(last_row) - 1):
            res.append(last_row[i] + last_row[i + 1])
        res += [1]
        return res
