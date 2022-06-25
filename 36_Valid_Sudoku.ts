function isValidSudoku(board: string[][]): boolean {
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            if (parseInt(board[i][j])) {
                if (
                    checkRow(board, [i, j], board[i][j]) &&
                    checkCol(board, [i, j], board[i][j]) &&
                    checkNine(board, [i, j], board[i][j])
                ) {
                    continue;
                } else {
                    return false;
                }   
            }
        }
    }
    return true;
};

function checkRow(board: string[][], cursor: [number, number], target: string): boolean {
    for (let col = 0; col < 9; col++) {
        if (col === cursor[1]) continue;
        if (board[cursor[0]][col] === target) return false;
    }
    return true
};
             
function checkCol(board: string[][], cursor: [number, number], target: string): boolean {
    for (let row = 0; row < 9; row++) {
        if (row === cursor[0]) continue;
        if (board[row][cursor[1]] === target) return false;
    }   
    return true
};
             
function checkNine(board: string[][], cursor: [number, number], target: string): boolean {
    let currRow = cursor[0] - (cursor[0] % 3);
    let currCol = cursor[1] - (cursor[1] % 3);
    
    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            if (currRow + i === cursor[0] && currCol + j === cursor[1] ) continue;
            if (board[currRow + i][currCol + j] === target) return false;
        }
    }
    return true
};
