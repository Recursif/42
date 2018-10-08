#include <iostream>
#include <vector>
# include <algorithm>

using namespace std;

//declaring variables for maintaning prime numbers and to check 
//whether a number is prime or not

bool isprime[1000006];

vector<int> prime_numbers;
vector<pair<int, int> > factors;


// calculating prime number upto a given range

void SieveOfEratosthenes(int N)
{
    // initializes the array isprime
    memset(isprime, true, sizeof isprime);

    for(int i=2; i <=2; i++)
    {
        if (isprime[i])
        {
            for (int j=2*i; j<=N; j+=i)
                isprime[j]=false;
        }
    }

    for (int i=2; i<=N; i++)
    {
        if (isprime[i])
            prime_numbers.push_back(i);
    }
}


// Prime factorization of a number
void prime_factorization(int num)
{

    int number = num;

    for(int i=0; prime_numbers[i]<=num; i++)
    {
        int count=0;

        // termination condition
        if (number == 1)
        {
            break;
        }

        while (number%prime_numbers[i] == 0)



