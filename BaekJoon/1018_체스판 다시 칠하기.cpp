
#include<stdio.h>
char comp[] = {'W', 'B'}; // compare character
int start = 0; // start is W or B 
int row = 0; 
int col = 0; // (row, col) start point
int min = 65; // changed Minimum

int main(void)
{
    int n, m;
    scanf("%d%d", &n, &m);

    char h[n][m];
    for(int i=0; i<n; i++)
    {
        scanf("%s", h[i]);
    }

    while(row + 8 <= n && col + 8 <= m)
    {
        for(int k=0; k<2; k++)
        {
            int cnt = 0;
            start = k;
            for(int i=row; i<row+8; i++)
            {
                for(int j=col; j<col+8; j++)
                {
                    if(h[i][j] != comp[start % 2])
                    {
                        cnt += 1;
                    }
                    start += 1;
                }
                start += 1;
            }
            if(cnt < min)
            {
                min = cnt;
            }
        }

        col += 1;
        if(col + 8 > m)
        {
            col = 0;
            row += 1;
        }
    }

    printf("%d", min);
    return 0;
}

/*
8 8
BBBBWBBW
WWWWBBWB
WWBBWBWW
WBWWBWBW
WBBWBBWB
BWBWBWWB
BWWWWWBW
BWBBBBWW
답 : 29
출력 : 35
 */

/* alex9801님의 답
#include <stdio.h>

char arr[50][51];

inline bool f(char a)
{
	return a=='W'?0:1;
}

int main()
{
	int x,y,cnt,mn=32,n,m,i,j;
	scanf("%d%d",&n,&m);
	for(i=0;i<n;i++)
		scanf("%s",arr[i]);
	for(i=0;i<n-7;i++)
	{
		for(j=0;j<m-7;j++)
		{
			cnt=0;
			for(x=i;x<i+8;x++)
				for(y=j;y<j+8;y++)
					cnt+=f(arr[x][y])==(x+y)%2;
			cnt=cnt>32?64-cnt:cnt;
			mn=cnt<mn?cnt:mn;
		}
	}
	printf("%d",mn);
	return 0;
}
 */