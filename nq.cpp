#include<iostream>
#include<vector>
using namespace std;

bool isSafe(int row, int col, vector<string> &board, int n){
    for(int i = 0; i < row; i++){
        if(board[i][col] == 'Q') return false;
    }

    for(int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--){
        if(board[i][j] == 'Q') return false;
    }

    for(int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++ ){
        if(board[i][j] == 'Q') return false;
    }

    return true;
}


void solve(int row, vector<string> &board, int n, vector<vector<string>> &res){
    if(row == n){
        res.push_back(board);
        return;
    }

    for(int col = 0; col < n; col++){
        if(isSafe(row, col, board, n)){
            board[row][col] = 'Q';
            solve(row + 1, board, n, res);
            board[row][col] = '.';
        }
    }
}

vector<vector<string>> solveNQueens(int n){
    vector<vector<string>> res;
    vector<string> board(n, string(n, '.'));
    solve(0, board, n, res);
    return res;
}

int main(){
    int n;
    cout<<"Enter N";
    cin>>n;
    vector<vector<string>> solutions = solveNQueens(n);
    for(auto& sol : solutions){
        for(auto& row : sol){
            cout<<row<<endl;
        }
        cout<<endl;
    }

    cout<<"Total solutions"<<solutions.size()<<endl;
}