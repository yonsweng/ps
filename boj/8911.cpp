#include <cstdio>
#include <cstring>

const struct direction {
	int x, y;
} d[] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
// up, right, down, left

int main()
{
	int t;
	scanf("%d", &t);
	for(int test_case=0; test_case<t; test_case++) {
		char command[500];
		scanf("%s", command);
		int len = strlen(command);

		int x_min = 0, x_max = 0, y_min = 0, y_max = 0;
		int x = 0, y = 0, dir = 0;

		for(int i=0; i<len; i++) {
			if(command[i] == 'F') {
				x += d[dir].x;
				y += d[dir].y;

				if(x < x_min) x_min = x;
				else if(x > x_max) x_max = x;
				if(y < y_min) y_min = y;
				else if(y > y_max) y_max = y;
			}
			else if(command[i] == 'B') {
				x -= d[dir].x;
				y -= d[dir].y;

				if(x < x_min) x_min = x;
				else if(x > x_max) x_max = x;
				if(y < y_min) y_min = y;
				else if(y > y_max) y_max = y;
			}
			else if(command[i] == 'L')
				dir = (dir + 1) % 4;
			else
				dir = (dir + 3) % 4;
		}

		printf("%d\n", (y_max - y_min) * (x_max - x_min));
	}
	
	return 0;
}