#include <iostream>

using namespace std;

long fib_even_sum(long x)
{
  // Fibonacci first 2 terms
  long a = 1;
  long b = 2;
  long temp;
  long sum = b;

  while(1)
  {
    // Calculate Fib next term
    temp = b;
    b = a + b;
    a = temp;

    // Fisrt check if new term exeeds barrier
    if (b >= x)
      break;

    // If new result is even, add to sum
    if (b%2 == 0)
      sum += b;
  }

  return sum;
}

// BEWARE: Test cases contain LARGE numbers that sometimes lead to overflow
int main()
{
    // Input and memory allocation
    long T;  // number of test cases
    cin >> T;
    long *inputs = new long[T];
    
    // Read N from keyboard and store it to a matrix for furter processing
    for(int i = 0; i < T; i++)
    {
      long int n;
      cin >> n;
      inputs[i] = n;
    }

    // Calculate and display result
    long result;

    for(int i = 0; i<T; i++)
    {
      result = fib_even_sum(inputs[i]);
      cout<<result<<"\n";
    }

    // Delete allocated matrix
    delete[] inputs;
    return 0;
}
