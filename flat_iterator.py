
class FlatIterator:
    def __init__(self, list_of_lists):
        self.res_list = list_of_lists
    
    def __iter__(self):
        self.cur_main = 0
        self.cur_nested = -1
        return self

    def __next__(self):
        self.cur_nested += 1
        if self.cur_nested >= len(self.res_list[self.cur_main]):
            self.cur_main += 1
            self.cur_nested = 0
        if self.cur_main >= len(self.res_list):
            raise StopIteration
        return self.res_list[self.cur_main][self.cur_nested]
