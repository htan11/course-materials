%% Solve the following LPP by graphical method.
%             Max Z = 3x1 + 5 x2
% Subject to:  x1 + 2x2 <= 2000,
%              x1 + x2  <= 1500,
%                   x2  <= 600,
%               x1>=0, x2>= 0.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
format short;
clear all;
clc;
%% Input Parameter
C=[3 5];
A=[1 2;1 1;0 1];
b=[2000;1500;600];
%% Phase 2: Plotting the graph
y1 = 0:1:max(b);
x21 = (b(1) - A(1,1).*y1)./A(1,2);
x22 = (b(2) - A(2,1).*y1)./A(2,2);
x23 = (b(3) - A(3,1).*y1)./A(3,2);
x21 = max(x21,0);
x22 = max(x22,0);
x23 = max(x23,0);
plot(y1,x21,'r',y1,x22,'k',y1,x23,'b');
xlabel('x1 values');
ylabel('x2 values');
legend('x1+2x2=2000','x1+x2=1500','x2=600');
grid on
%% find the corner points with the axes
Cx1 = find(y1 == 0);
C1 = find(x21 == 0);
Line1 = [y1(:,[C1,Cx1]);x21(:,[C1,Cx1])]';
C2 = find(x22 == 0);
Line2 = [y1(:,[C2,Cx1]); x22(:,[C2,Cx1])]';
C3 = find(x23 == 0);
Line3 = [y1(:,[C3,Cx1]); x23(:, [C3,Cx1])]';
corpoint = unique([Line1;Line2;Line3],'rows');
%% Find the point of intersections
HG = [0;0];
for i=1:size(A,1)
    hg1 = A(i,:);
    b1 = b(i,:);
    for j=i+1:size(A,1)
        hg2 = A(j,:);
        b2 = b(j,:);
        Aa = [hg1;hg2];
        Bb = [b1;b2];
        Xx = Aa\Bb;
        HG = [HG Xx];
    end
end
pt = HG';
%% Write all corner points
allpt = [pt;corpoint];
points = unique(allpt,'rows');
%% Find the feasible region
PT = contraints(points);
PT = unique(PT,'rows');
%% Compute objective function
for i=1:size(PT,1)
    Fx(i,:) = sum(PT(i,:).*C);
end
Vert_Fn = [PT, Fx];
%% Find the optimal one
[fxval, indfx] = max(Fx);
Optval = Vert_Fn(indfx,:);
OPTIMAL_BFS = array2table(Optval);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function retval = contraints(X)
x1 = X(:,1);
x2 = X(:,2);
const1 = x1 + 2.*x2 - 2000;
h1 = find(const1 > 0);
X(h1,:) = [];
x1 = X(:,1);
x2 = X(:,2);
const2 = x1 + x2 -1500;
h2 = find(const2 > 0);
X(h2,:) = [];
x1 = X(:,1);
x2 = X(:,2);
const3 = x2 - 600;
h3 = find(const3 > 0);
X(h3,:) = [];
retval = X;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%