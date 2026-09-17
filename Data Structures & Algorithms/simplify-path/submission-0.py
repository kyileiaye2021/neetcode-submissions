class Solution:
    def simplifyPath(self, path: str) -> str:
        # happy case
        # /neetcode.com
        # /neetcode.com

        # ///neetcode.com
        # /neetcode.com

        # /../neetcode.com/practice//
        # /neetcode.com/practice

        # edge cases

        # /....neetcode.com//practice../.
        # /....neetcode.com/practice

        # /..//.
        # /
        #stack

        # /, ., ..
        # curr temp str between slashes and check that is .. or . or empty
        # we can ignore empty or .
        # if .. , we have to pop the stack if there are ele in stack

        stack = []
        curr = ""
        path += '/'
        for i in range(len(path)):
            if path[i] == '/':
                if curr == '..':
                    # pop the last curr out
                    if stack:
                        stack.pop()
                
                elif curr != '.' and curr != '':
                    stack.append(curr)

                curr = ''

            else:
                curr += path[i]
        
        return '/' + '/'.join(stack)

    
