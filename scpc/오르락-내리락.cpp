/*
You should use the standard input/output

in order to receive a score properly.

Do not use file input and output

Please be very careful. 
*/

#include <cstdio>

int Answer;
int work[1000001];
int accumul[1000001];

int main(int argc, char** argv)
{
	int T, test_case;
	/*
	   The freopen function below opens input.txt file in read only mode, and afterward,
	   the program will read from input.txt file instead of standard(keyboard) input.
	   To test your program, you may save input data in input.txt file,
	   and use freopen function to read from the file when using cin function.
	   You may remove the comment symbols(//) in the below statement and use it.
	   Use #include<cstdio> or #include <stdio.h> to use the function in your program.
	   But before submission, you must remove the freopen function or rewrite comment symbols(//).
	 */	

	//freopen("input.txt", "r", stdin);

    work[1] = 0;
    work[2] = 1;
    for(int i=4; i<=1000000; i+=2) {
        work[i] = work[i/2] + 1;
        work[i-1] = work[i] + 1;
    }

    accumul[0] = 0;
    for(int i=1; i<=1000000; i++) {
        accumul[i] = accumul[i-1] + work[i];
    }

    scanf("%d", &T);
	for(test_case = 0; test_case  < T; test_case++)
	{

		Answer = 0;
		/////////////////////////////////////////////////////////////////////////////////////////////
        int n1, n2;
        scanf("%d %d", &n1, &n2);

        Answer = accumul[n2] - accumul[n1-1];
		/////////////////////////////////////////////////////////////////////////////////////////////
		
		// Print the answer to standard output(screen).
        printf("Case #%d\n", test_case+1);
        printf("%d\n", Answer);
	}

	return 0;//Your program should return 0 on normal termination.
}