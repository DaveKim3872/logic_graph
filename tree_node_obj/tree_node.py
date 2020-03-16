class Node():
    def __init__(self, val, and_con = False, sel = False):
        self.sons = []  # 子节点列表
        self.con = and_con  # 子节点与或条件（默认为False）
        self.value = val # 节点名称
        self.select = sel # 节点是否被选择（默认为False）
        # self.share = share # 共享节点（默认为空列表）
        # self.id = id # 节点ID初始为0
        # self.count = 0 # 总节点数计数
    
    def search(self, val):
        if val == self.value:
            print('查找到当前操作节点为：' + str(self.value))
            return self
        else:
            for item in self.sons:
                a = item.search(val)
                if a:
                    return a

    def insert(self, pos, val, and_con = False):
        # self.sons.append(Node(val, and_con))
        val_dupl = self.search(val)
        position = self.search(pos)
        if not position:
            return False
        if val_dupl:
            node_to_ins = val_dupl
        else:
            node_to_ins = Node(val, and_con)
        position.sons.append(node_to_ins)
        print('成功插入节点：' + str(val))
        print("")
        return True

    def delete(self, val):
        node = self.search(val)
        if node:
            del node
