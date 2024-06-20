#include <stdio.h>

int main()
    {
     int t=0, a[]={0,1,2};
     for(int i=0;i<3;i++) 
      {
      for(int j=0;j<3;j++){
            printf("i=%d, j=%d, t=%d \n",i,j,t++);
        }
      }
    }

