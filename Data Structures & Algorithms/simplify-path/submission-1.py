class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        stack = []
        for i in path :
            if i == ".." :
                if stack :
                    stack.pop()
                    stack.pop()
            elif i != "" and i != ".":
                stack.append('/')
                stack.append(i)
            print(stack)
        if not stack:
            stack.append('/')
        
        return ("").join(stack)
            