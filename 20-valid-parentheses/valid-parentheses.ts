function isValid(s: string): boolean {
    const validMap: Record<string, string> = {
        ")": "(",
        "}": "{",
        "]": "["
    }    
    const stack: string[] = [];

    for (const char of s) {
        if (char in validMap) {
            if (stack.at(-1) === validMap[char]) {
                stack.pop()
            } else {
                return false
            }
        } else {
            stack.push(char)
        }
    }

    return stack.length === 0
};