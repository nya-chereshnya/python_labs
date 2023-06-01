#include <iostream>
#include <string.h>
#include <cmath>

using namespace std;

extern "C" double **taylor_ln_function(int x1, int x2, int deltax, double E)
{
    double **res = new double *[((x2 - x1) / deltax)];
    double result, diff;
    int i = 0;
    for (int x = x1; x < x2; x += deltax)
    {
        res[i] = new double[3];
        result = 0;
        diff = 1;
        int n = 0;
        while (diff > E)
        {
            diff = 1 / ((2 * n + 1) * pow((2 * x + 1), (2 * n + 1)));
            result += diff;
            n += 1;
        }
        res[i][0] = x;
        res[i][1] = result * 2;
        res[i][2] = n;
        i++;
    }
    return res;
}

int main()
{
}