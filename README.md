# hello-world
#include "stdafx.h"
#include <iostream>
using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{
	float mas[2][4];
	int i, j;
	int n = 4;
	for (i = 0; i < 2;i++)
	for (j = 0; j < 4; j++)
		cin >> mas[i][j];
	float sumx=0;
	float sumy=0;
	float sumxy=0;
	float sumxx = 0;
	for (j = 0; j < 4; j++)
	{
		sumx += mas[0][j];
		sumy += mas[1][j];
		sumxy += mas[0][j] * mas[1][j];
		sumxx += mas[0][j] * mas[0][j];
	}
	double a;
	double b;
	a = (n*sumxy - (sumx*sumy))/(n*sumxx-sumx*sumx);
	b = (sumy - (a*sumx))/n;
	double pog=0;
	for (j = 0; j < 4; j++)
	{
		pog += (mas[1][j] - (a*mas[0][j] + b))*(mas[1][j] - (a*mas[0][j] + b));
	}
	cout << "a =" << a << '\n';
	cout << "b =" << b << '\n';
	cout << "pog ="<< pog<<'\n';
	
	system("pause");
	return 0;
	
}
