clc
clear all
format short
syms  x1 x2;
f1 = x1 - x2 + 2*x1^2 + 2*x1*x2 + x2^2;
fx = inline(f1);
fobj = @(x) fx(x(:,1), x(:,2));
%% Gradient of f
grad = gradient(f1);
G = inline(grad);
gradx = @(x) G(x(:,1), x(:,2));
%% Hessian Matrix
H1 = hessian(f1);
Hx = inline(H1);
%% Steepest Descent Method
tol = 1e-3;
x0 = [1,1];
maxiter = 4;
X = [];
iter = 0;
while norm(gradx(x0))>tol && iter < maxiter
    X = [X; x0];
    H = Hx(x0);
    S = -gradx(x0);
    lambda = S'*S./(S'*H*S);
    Xnew = x0 + lambda.*S';
    x0 = Xnew;
    iter = iter + 1;
end

%% Print the Solution
fprintf('Optimal Solution X =[%f, %f]\n', x0(1), x0(2));
fprintf('Optimal Value f(x) = %f \n', fobj(x0));
