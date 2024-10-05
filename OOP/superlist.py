class SuperList(list):
    list_init = []

    def __len__(self):
        return 1000


my_list = SuperList()

print(len(my_list))
