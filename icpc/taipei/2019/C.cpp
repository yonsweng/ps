#include <iostream>

int arr[50];

int main()
{
    int n;
    scanf("%d", &n);

    for (int i = 0; i < n; ++i)
        scanf("%d", arr+i);

    bool yes = true;
    for (int i = 0; i < n && yes; ++i)
    {
        for (int j = 0; j < n && yes; ++j)
        {
            for (int k = 0; k < n && yes; ++k)
            {
                if (i == j || j == k || k == i)
                    continue;
                if ((arr[i]-arr[j]) % arr[k] != 0)
                    yes = false;
            }
        }
    }

    if (yes)
        printf("yes");
    else
        printf("no");

    return 0;
}