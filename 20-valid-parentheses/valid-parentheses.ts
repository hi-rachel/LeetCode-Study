function isValid(s: string): boolean {
    const validMap = {
        ")": "(",
        "}": "{",
        "]": "["
    }    
    const openParentheses = ["(", "{", "["]
    const stack = [];

    for (const char of s) {
        if (openParentheses.includes(char)) {
            stack.push(char)
        } else {
            if (stack.at(-1) === validMap[char]) {
                stack.pop()
            } else {
                return false
            }
        }
    }

    return stack.length === 0
};