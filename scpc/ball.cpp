#include <cstdio>
#include <cmath>  // M_PI, acos()

double Answer;

int main(int argc, char** argv)
{
	int T, test_case;

	//freopen("input.txt", "r", stdin);

	scanf("%d", &T);
	for(test_case = 0; test_case  < T; test_case++)
	{
		/////////////////////////////////////////////////////////////////////////////////////////////
        int R, S, E, N;
		scanf("%d %d %d\n", &R, &S, &E);
        scanf("%d\n", &N);

        Answer = E - S;

        for(int i=1; i<=N; i++) {
            int l, r, h;
            scanf("%d %d %d\n", &l, &r, &h);

            if(h >= R) {
                Answer += 2 * (h - R) - 2 * R + M_PI * R;
            }
            else {
                Answer += 2 * R * (acos((R-h)/(double)R) - sin(acos((R-h)/(double)R)));
            }
        }
		/////////////////////////////////////////////////////////////////////////////////////////////
		
		// Print the answer to standard output(screen).
        printf("Case #%d\n%.8lf\n", test_case+1, Answer);
	}

	return 0;//Your program should return 0 on normal termination.
}