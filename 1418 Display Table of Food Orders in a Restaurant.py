from typing import List
from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = sorted(set(x[2] for x in orders))
        table_set = sorted(set(x[1] for x in orders), key=lambda x: int(x))
        display = []

        my_dict = {table: [0] * len(foods) for table in table_set}
        index_table = {x[1]: x[0] for x in enumerate(foods)}

        head = ['Table']
        head.extend(foods)
        display.append(head)

        for order in orders:
            table, food = order[1], order[2]
            my_dict[table][index_table[food]] += 1

        for k, v in my_dict.items():
            my_list = [k]
            my_list.extend(map(str, v))
            display.append(my_list)

        return display

a = Solution()
a.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]])