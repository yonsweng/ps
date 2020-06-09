//
//  main.cpp
//  boj2473
//
//  Created by 최연웅 on 2018. 9. 24..
//  Copyright © 2018년 최연웅. All rights reserved.
//

#include <iostream>
#include <algorithm>

int main(int argc, const char * argv[]) {
    // insert code here...
    int n, d[5000];
    std::cin >> n;
    for(int i=0; i<n; i++){
        std::cin >> d[i];
    }
    
    std::sort(d, d+n);
    
    int result[3];
    long long m = 9999999999;
    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1; j++) {
            int left = j+1, right = n;
            while(left < right) {
                int center = (left + right) / 2;
                long long sum = (long long)d[i]+d[j]+d[center];
                
                if(abs(sum) < m) {
                    m = abs(sum);
                    result[0] = d[i]; 
                    result[1] = d[j];
                    result[2] = d[center];
                }
                
                if(sum > 0){
                    right = center;
                } else {
                    left = center + 1;
                }
            }
        }
    }
    
    std::cout << result[0] << " " << result[1] << " " << result[2];
    
    return 0;
}
