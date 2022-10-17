#include<stdio.h>

int main(){
    int n = 5;
    int sum = 0;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            sum += i;
        }
    }
    if(sum>10000){
        printf("go\n");
    }
    printf("%d", sum);
    
}