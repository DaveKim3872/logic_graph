from tree_node_obj.tree_node import Node
import pickle

def condition(origin_in):
    if origin_in == 'T':
        return True
    elif origin_in == 'F':
        return False
    else:
        print("格式错误！请重新输入(T/F): ")
        new_in = input()
        return condition(new_in)

print("1.新建逻辑树")
print("2.读取逻辑树")
print("请选择: ", end = "")
op = int(input())
print("")

if op == 1:
    print("建立逻辑图，请输入根节点名称: ", end = "")
    val = str(input())
    print("")
    print("请输入根节点是否需要\"与\"条件(T/F): ", end = "")
    and_con = condition(input())
    print("")
    n = Node(val, and_con)
elif op == 2:
    print("请输入文件名称: ", end = "")
    input_dir = 'graph_data\\' + str(input())
    with open(input_dir, 'rb+') as f:
        n = pickle.load(f)
else:
    print("输入错误！")
    exit()


print("1.插入节点")
print("2.删除节点")
print("3.退出操作")
print("请选择操作:", end = "")
op = int(input())
print("")
while op != 3:
    if op == 1:
        print("选择父节点:", end = "")
        pos = str(input())
        print("")
        print("新节点名称:", end = "")
        val = str(input())
        print("")
        print("新节点是否需要\"与\"条件(T/F):", end = "")
        and_con = condition(input())
        print("")
        # n.insert(pos, val, and_con)
        a = n.insert(pos, val, and_con)
        if not a:
            print("程序输入有误，请重新运行！")
            break
    else:
        print("输入节点名称:", end = "")
        val = str(input())
        print("")
        n.delete(val)

    print("1.插入节点")
    print("2.删除节点")
    print("3.退出操作")
    print("请选择操作:", end = "")
    op = int(input())
    print("")

flg = 'graph_data\\logic_tree.pkl' 
with open(flg, 'wb+') as f:  
    picklestring = pickle.dump(n, f)   # read file and build object