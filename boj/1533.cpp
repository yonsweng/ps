//
//  main.cpp
//  boj1533
//
//  Created by 최연웅 on 2018. 9. 22..
//  Copyright © 2018년 최연웅. All rights reserved.
//

#include <iostream>

#define DIV 1000003

using namespace std;

int** alloc_matrix(int n)
{
    int **m = (int**)malloc(n*sizeof(int*));
    for(int i = 0; i < n; i++) {
        m[i] = (int*)malloc(n*sizeof(int));
    }
    return m;
}

void free_matrix(int **m, int n)
{
    for(int i = 0; i < n; i++) {
        free(m[i]);
    }
    free(m);
}

void copy(int **dst, int **src, int n)
{
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            dst[i][j] = src[i][j];
        }
    }
}

int** matmul(int **a, int **b, int n)
{
    int **c = alloc_matrix(n);
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            int sum = 0;
            for(int k = 0; k < n; k++) {
                sum += (a[i][k] % DIV) * (b[k][j] % DIV) % DIV;
            }
            c[i][j] = sum;
        }
    }
    
    return c;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int **d;
    int g[10][10];
    int n, s, e, t;
    cin >> n >> s >> e >> t;
    s--; e--;
    for(int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        for(int j = n-1; j >= 0; j--) {
            g[i][j] = tmp % 10;
            tmp /= 10;
        }
    }
    
    int cnt = n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(g[i][j] > 1)
                cnt += g[i][j] - 1;
        }
    }
    
    d = alloc_matrix(cnt);
    
    int next = n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(g[i][j] > 1) {
                int former = i;
                for(int k = 1; k < g[i][j]; k++) {
                    d[former][next] = 1;
                    former = next++;
                }
                d[former][j] = 1;
            }
            else {
                d[i][j] = g[i][j];
            }
        }
    }
    
    int **m[30], b[30], digit = 0, t0 = t;
    
    while(t0 > 0) {
        b[digit] = t0 % 2;
        t0 /= 2;
        m[digit] = alloc_matrix(cnt);
        copy(m[digit], d, cnt);
        int **tmp = matmul(d, d, n);
        free_matrix(d, n);
        d = tmp;
        
        digit++;
    }
    
    for(int k = 0; k < digit; k++) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                printf("%d ", m[k][i][j]);
            }
            printf("\n");
        }
        printf("\n");
    }
    
    free_matrix(d, cnt);
    for(int i = 0; i < digit; i++) {
        free_matrix(m[i], cnt);
    }
    
    return 0;
}

