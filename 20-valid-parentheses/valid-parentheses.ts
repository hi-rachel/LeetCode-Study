function isValid(s: string): boolean {
    const matchChar: { [key: string]: string } = {'(': ')', "{": "}", "[": "]"};
    const stack: string[] = [];

    for (const char of s) {
         const test = stack[stack.length - 1];
         
        if (matchChar[test] === char) {
            stack.pop()
        } else {
            stack.push(char)
        }
    }
       
    return stack.length === 0;
};