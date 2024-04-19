int a = 4;
int b = 8;
int c = 0;
c = a + b / b - a;
if(c < 0)
c = c + 2;
else
c = c - 1;
Console.WriteLine(c);