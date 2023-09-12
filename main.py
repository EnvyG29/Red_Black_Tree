from Red_Black_Tree import RBTree


def go():
    """Свои хотелки пишем тут"""

    tree_str = RBTree()
    tree_str.insert("apple")
    tree_str.insert("java")
    tree_str.insert("bullet")
    tree_str.insert("soup")
    tree_str.insert("tree")
    tree_str.insert("code")
    tree_str.insert("python")
    tree_str.insert("078")
    tree_str.insert(True)

    tree_str.print_tree()
    print()
    tree_digit = RBTree()

    tree_digit.insert(10)
    tree_digit.insert(20)
    tree_digit.insert(40)
    tree_digit.insert(60)
    tree_digit.insert(50.5)
    tree_digit.insert(80)
    tree_digit.insert(60)
    tree_digit.insert("100")
    tree_digit.insert(45)
    tree_digit.insert(90)
    tree_digit.insert(100)
    tree_digit.insert(45)
    tree_digit.insert(90)
    tree_digit.insert(25)
    tree_digit.print_tree()
    print()
    print(tree_digit.to_list(), tree_str.to_list(), sep="\n")
    print(">>> ", tree_str.search("python"))
    print(">>> ", tree_str.search("Python"))
    print(">>> ", tree_digit.search(40))
    tree_digit.delete(20)

    tree_digit.print_tree()


def go2():
    tree_digit = RBTree()
    print("Red_Black_Tree\n"
          "45 - введите число что добавить его в дерево\n"
          "stop - закончить программу\n"
          "list - выведет дерево в виде списка\n"
          "del 66 - удалит число из дерева")
    while True:
        print()
        a = input(">>> ")
        if a == "stop":
            return
        if a == "list":
            print(tree_digit.to_list())
        elif a[0:4] == "del " and a[4:].isdigit():
            tree_digit.delete(int(a[4:]))
            print()
            tree_digit.print_tree()
        elif a.isdigit():
            tree_digit.insert(int(a))
            print()
            tree_digit.print_tree()
        else:
            print("Невалидная команда или число")


if __name__ == '__main__':
    # go()
    go2()
