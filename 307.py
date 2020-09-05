class NumArray:
    class Node:
        def __init__(self, value, start, stop, parent=None, left=None, right=None):
            self.value = value
            self.start = start
            self.stop = stop
            self.parent = parent
            self.left = left
            self.right = right

    def __init__(self, nums: List[int]):
        if not nums:
            self.root = None
            return

        self.root = self._build_tree(nums, 0, len(nums) - 1, None)

    def update(self, i: int, val: int) -> None:
        if self.root is None:
            return

        p = self.root
        while p.start != p.stop or p.start != i:
            mid = (p.start + p.stop) // 2
            if i <= mid:
                p = p.left
            else:
                p = p.right

        diff = val - p.value

        while p:
            p.value += diff
            p = p.parent

    def sumRange(self, i: int, j: int) -> int:
        if self.root is None:
            return

        p = self.root
        return self._search(p, i, j)

    def _build_tree(self, nums, start, stop, parent):
        if start == stop:
            node = self.Node(nums[start], start, stop, parent)
            return node

        mid = (start + stop) // 2
        node = self.Node(0, start, stop, parent)
        left = self._build_tree(nums, start, mid, node)
        right = self._build_tree(nums, mid + 1, stop, node)
        node.value = left.value + right.value
        node.left = left
        node.right = right

        return node

    def _search(self, node, i, j):
        if i == node.start and j == node.stop:
            return node.value

        mid = (node.start + node.stop) // 2

        if j <= mid:
            return self._search(node.left, i, j)
        elif i > mid:
            return self._search(node.right, i, j)
        else:
            return self._search(node.left, i, mid) + self._search(node.right, mid + 1, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)