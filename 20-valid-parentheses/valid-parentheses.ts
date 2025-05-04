function isValid(s: string): boolean {
    const stack: string[] = [];
    const parentheseMap: Record<string, string> = {
        ")": "(",
        "]": "[",
        "}": "{",
    }

    for (const char of s) {
        if (["(", "[", "{"].includes(char)) {
            stack.push(char);
        } else {
            if (stack.pop() !== parentheseMap[char]) return false;
        }
    }
    return stack.length === 0;
}