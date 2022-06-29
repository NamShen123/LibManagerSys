class Convert_to_list:
    header = None
    body = None

    def listdict_to_list(self, list_dict, lst=True):
        if lst:
            self.header = list(list_dict[0].keys())
            list_val = []
            for dict in list_dict:
                list_val.append(list(dict.values()))
            self.body = list_val
        else:
            self.header = list(list_dict.keys())
            self.body = list(list_dict.values())

# a = [{"key1": "val1a", "key2": "val2a"}, {"key1": "val1b", "key2": "val2b"}, {"key1": "val1c", "key2": "val2c"}]
# b = Convert_to_list()
# b.listdict_to_list(a)
# print(b.header)
# print(b.body)