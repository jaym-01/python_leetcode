class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def get_bin(root):
            if root:
                return str(root.val)
            else:
                return "null"
        queue = deque()
        queue.append(root)

        out = []

        while len(queue) > 0:
            cur = queue.popleft()
            out.append(get_bin(cur))

            if cur == None:
                continue
            else:
                queue.append(cur.left)
                queue.append(cur.right)
        
        s_out = ",".join(out)
        return s_out

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def get_val(d):
            if d == "null":
                return None
            else:
                return TreeNode(int(d))
        print(data)

        its = deque(data.split(","))
        q = deque()

        if len(its) == 0:
            return None
        else:
            head = get_val(its.popleft())
            q.append(head)

        while len(its) > 0:
            cur = q.popleft()
            l = get_val(its.popleft())
            r = get_val(its.popleft())

            if not cur:
                continue
            else:
                cur.left = l
                cur.right = r

                if l: q.append(l)
                if r: q.append(r)

        return head
