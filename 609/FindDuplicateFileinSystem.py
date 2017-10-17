class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        content_map = {}
        for path in paths:
            file_list = path.split(" ")
            file_path = file_list[0]
            for file_desc in file_list[1:]:
                idx1 = file_desc.find('(')
                idx2 = file_desc.find(')')
                file_name = file_desc[0: idx1]
                file_content = file_desc[idx1 + 1: idx2]
                # print file_name, file_content
                new_file_name = "/".join([file_path, file_name])
                if file_content not in content_map:
                    content_map[file_content] = [new_file_name]
                else:
                    content_map[file_content].append(new_file_name)
        duplicate = []
        for (k,v) in content_map.items():
            if len(v) > 1:
                duplicate.append(v)
        return duplicate


if __name__ == '__main__':
    s = Solution()
    A = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
    print s.findDuplicate(A)
