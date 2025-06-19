function findCircleNum(isConnected: number[][]): number {
    const n = isConnected.length;
    const visited: boolean[] = Array(n).fill(false);

    function dfs(node: number) {
        visited[node] = true;
        for (let neighbor = 0; neighbor < n; neighbor++) {
            if (isConnected[node][neighbor] === 1 && !visited[neighbor]) {
                dfs(neighbor);
            }
        }
    }

    let components = 0;
    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i)
            components++;
        }
    }
    return components;
};