% assigning the input function and the values of n and y from 0-199
n = 0:199;
x = input('input x(n):');
y = 0:199;
%looping statement for the function 
for z=1:length(n)
if n(z) == 0
    y(z) = -1.5*x(z) + 2*x(z+1)- 0.5*x(z+2);
   
elseif n(z) < 199 %if n(z) is <198
    y(z) = 0.5*x(z+1) - 0.5*x(z-1);
 
else %if n(z) is not =0 and n is <198
    y(z) = 1.5*x(z) - 2*x(z-1) + 0.5*x(z-2);
    
% end of looping statement
end
end
%plotting the function using  plot and labeling the graph
plot(n,x,'g--');
xlabel 'x(n)'
ylabel 'y(n)'
hold on
plot(n,y,'m--');
title ('plot of x(n) and y(n)')
legend('x','y')
grid


