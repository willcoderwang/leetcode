class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        input_list = []

        pre = '-'
        depth = 0
        num = ''

        for i in range(len(S)):
            if S[i] != '-':
                num += S[i]
            else:
                if pre == '-':
                    depth += 1
                else:
                    input_list.append({'node': TreeNode(num), 'depth': depth})
                    num = ''
                    depth = 1

            pre = S[i]
        else:
            input_list.append({'node': TreeNode(num), 'depth': depth})

        import pdb; pdb.set_trace()
        pre_e = None
        root = None
        stack = []
        for e in input_list:
            node = e['node']

            if not pre_e:
                root = node

                pre_e = e
                continue

            if e['depth'] == pre_e['depth'] + 1:
                pre_e['node'].left = node
                stack.append(pre_e)

            else:
                pop_item = stack.pop()
                while e['depth'] != pop_item['depth'] + 1:
                    pop_item = stack.pop()
                pop_item['node'].right = node

            pre_e = e

        return root
