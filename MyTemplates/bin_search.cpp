#include <bits/stdc++.h>
using namespace std;

int main(){

    int a[] = { 1, 5, 8, 9, 6, 7, 3, 4, 2, 0 };
    int asize = sizeof(a) / sizeof(a[0]);

    sort(a, a + asize);
    if(binary_search(a, a + 10, 2)){
    	printf("found\n");
    }

	return 0;

}
