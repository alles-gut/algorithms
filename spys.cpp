//programers.co.kr
//Hash - 위장

#include <string>
#include <vector>
int a[31] = { 0, };
int v[31];
using namespace std;
 
int solution(vector<vector<string>> clothes) {
    int answer = 0;
    int size ;
    int ret = 1;
    size = clothes.size();
    for(int i =0 ;i<31; i++)
    {
        v[i] = 0;
    }
    for(int i = 0; i<size; i++)
    {
         if(v[i] == 1)
                continue;    
         for(int j = i ; j<size; j++)
         {
            if(clothes[i][1] == clothes[j][1] )
            {
                a[i]++; // i번째 종류 증가
                v[j]= 1;
            }
        }
    }
    for(int i = 0 ; i< 31; i++)
    {
        if(a[i]>0)
        {
            ret *= (a[i] +1);
        }
    }
    answer = ret - 1;
    return answer;
}
