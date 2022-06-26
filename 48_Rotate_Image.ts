/**
 Do not return anything, modify matrix in-place instead.
 */
function rotate(matrix: number[][]): void {
    let dict = {};
    
    for (let i = 0; i < matrix.length ; i++) {
        dict[i] = [...matrix[i]];
    }

    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix.length; j++) {
            matrix[j][matrix.length - 1 - i] = dict[i][j];
        }
    }
};
