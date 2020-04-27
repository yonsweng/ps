#include <cstdio>

int main()
{
	int a, b;
	scanf("%d %d", &a, &b);

	double c = (double)a / b;

	printf("%.11lf", c);

	return 0;
}