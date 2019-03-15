#include <bits/stdc++.h>
using namespace std;

int main(){

	set <int, greater <int> > myset;
	set <int, greater <int> > :: iterator itr;


	myset.insert(10);
	myset.insert(2);

	for(itr = myset.begin(); itr!=myset.end(); itr++){

		printf("%d \n", *itr);
	}

	printf("END\n");

	return 0;

}
