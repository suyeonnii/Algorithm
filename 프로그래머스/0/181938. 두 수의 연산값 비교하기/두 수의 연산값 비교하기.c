#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(int a, int b) {
    int answer = 0;
    
    // 정수를 문자열로 변환
    char aa[12]; 
    char bb[12]; 
    sprintf(aa, "%d", a);
    sprintf(bb, "%d", b);
    
    // 두 문자열을 합쳐서 정수로 변환
    char aabb_str[24]; // 충분한 공간 할당
    strcpy(aabb_str, aa);
    strcat(aabb_str, bb);
    int aabb = atoi(aabb_str);
    
    // 계산값
    int aabb2 = 2 * a * b;
    
    // 더 큰 값 반환
    if (aabb > aabb2 || aabb == aabb2)
        answer = aabb;
    else
        answer = aabb2;
        
    return answer;
}
