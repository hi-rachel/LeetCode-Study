function isValid(s: string): boolean {
    let prevLength = -1;

    while (s.length !== prevLength) {
        prevLength = s.length;
        s = s.replace("()", "").replace("[]", "").replace("{}", "");
    }

    return s.length === 0;
}