class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        from functools import cmp_to_key

        def comp(item1, item2):
            if item1[0] != item2[0]:
                return item1[0] - item2[0]
            else:
                return -(item1[1] - item2[1])
        people.sort(key=cmp_to_key(comp))
        for idx, item in enumerate(people):
            if idx > item[1]:
                people = people[:item[1]] + [item] + \
                    people[item[1]:idx] + people[idx + 1:]
        return people
