class SnapshotArray(object):

    def __init__(self, n):
        # set up histories so that each index has its own history
        self.histories = [[[-1, 0]] for _ in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.histories[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        left, right, pos = 0, len(self.histories[index])-1, -1
        while left <= right:
            mid = (left+right) // 2
            if self.histories[index][mid][0] <= snap_id:
                left = mid + 1
                pos = mid
            else:
                right = mid - 1
        return self.histories[index][pos][1]
    
snapshotArray = SnapshotArray(1)
snapshotArray.set(0, 4)
snapshotArray.set(0, 16)
snapshotArray.set(0, 13)
snapshotArray.snap()
snapshotArray.get(0, 0)
snapshotArray.snap()
