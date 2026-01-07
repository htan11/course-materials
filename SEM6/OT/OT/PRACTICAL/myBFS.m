format short
clear all
clc
%% Phase I: Input the parameters
C = [10, 8, 5, 11];
A = [2, 6, 1, 4; 1, -2, 5, 7];
b = [10; 15];
%% Phase II: Find the number of variables
m = size(A,1);  % Number of contraints
n = size(A,2);  % Number of variables
%% Phase III: Find the number of BFS and pairs of BFS
nb = nchoosek(n,m);
np = nchoosek(1:n,m);
%% Phase IV: Construct the basic solutions
solution = [];
for i = 1:nb
    y = zeros(n,1);
    x = A(:, np(i,:))\b;
    if all(x>=0 & x ~=inf & x~=-inf)
    y(np(i,:)) = x;
    solution = [solution, y];
    end
end
%% Phase V: Values of the objective functions
Z = C*solution;
%% Phase VI: Finding the optimal value
[Zmax, Zind] = max(Z);
BFS = solution(:, Zind);
%% Print all the solution
Optval = [BFS' Zmax];
OPTIMAL_BFS = array2table(Optval);
OPTIMAL_BFS.Properties.VariableNames(1:size(OPTIMAL_BFS,2))={'x_1','x_2','x_3','x_4','Value of Z'}