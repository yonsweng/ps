#include <iostream>
#include <algorithm>

using namespace std;

int Answer;

int main(int argc, char** argv)
{
	int T, test_case;
	cin >> T;
	
	for(test_case = 0; test_case  < T; test_case++) {
	    int N, K, A[200000], B[200000];
	    Answer = 0;
	    
	    cin >> N >> K;
	    for(int i=0; i<N; i++) cin >> A[i];
	    for(int i=0; i<N; i++) cin >> B[i];
	    
	    sort(A, A + N);
	    sort(B, B + N);
	    
	    for(int i=0; i<K; i++)
	        Answer = max(A[i] + B[K-i-1], Answer);
	    
		cout << "Case #" << test_case+1 << endl;
		cout << Answer << endl;
	}

	return 0;
}