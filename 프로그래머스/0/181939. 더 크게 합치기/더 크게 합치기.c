#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int solution(int a, int b) {
    int answer = 0;
    
    char ab[24];
    char ba[24];
    sprintf(ab,"%d%d",a,b);
    sprintf(ba,"%d%d",b,a);
    
    int num_ab=atoi(ab);
    int num_ba=atoi(ba);
    
    if(num_ab>num_ba||num_ab==num_ba)
        answer=num_ab;
    else
        answer=num_ba;
    
    return answer;
}