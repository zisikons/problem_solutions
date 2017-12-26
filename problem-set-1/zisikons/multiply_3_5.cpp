#include <iostream>

using namespace std;

// Given a number N and a divisor m, this function calculates and
// returns the sum of multiplies of m up to the number N.
long int sum_of_multiplies(long int N, int m)
{
  // Step 1: Calculate how many multiplies of m there are up to N
  long int num_of_multiplies = N/m;

  // Step 2: Calculate the sum of them (it's the sum of an arithmetic
  //         sequence from 1 to num_of multiplies, multiplied by m)
  return  m*num_of_multiplies*(num_of_multiplies+1)/2;
}

// BEWARE: Test cases contain LARGE numbers that sometimes lead to overflow
int main()
{
    // Input
    long int t;
    cin >> t;
    long int *inputs = new long int[t];
    
    // Read N from keyboard and store it to a matrix for furter processing
    for(int i = 0; i < t; i++)
    {
      long int n;
      cin >> n;
      inputs[i] = n;
    }
    
    // For every input print the result
    for(int i = 0; i < t; i++)
    {
      long int result;
      result =  sum_of_multiplies(inputs[i]-1,3) 
              + sum_of_multiplies(inputs[i]-1,5)
              - sum_of_multiplies(inputs[i]-1,15);
      cout<<result<<"\n";
    }

    // Delete allocated matrix
    delete[] inputs;
    return 0;
}
