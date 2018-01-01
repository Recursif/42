#include <stdlib.h>
#include <unistd.h>

int  valid_input(int N, int M1, int M2)
{
  return(N >= 1 && N <= 1000000 && \
    0 <= M1 && M1 < M2 && M2 <= N);
}

void print_influence(int N, int M1, int M2)
{
  if ((M1 + M2) / 2 < N / 2)
  {
    write(1, "2", 1);
  }
  else if ((M1 + M2) / 2 > N / 2)
  {
    write(1, "1", 1);
  }
  else
  {
    write(1, "0", 1);
  }
}

int  main(int argc, char **argv)
{
  int   N;
  int   M1;
  int   M2;

  if (argc == 4)
  {
    N = atoi(argv[1]);
    M1 = atoi(argv[2]);
    M2 = atoi(argv[3]);
    if (valid_input(N, M1, M2))
    {
      print_influence(N, M1, M2);
    }
  }
  return (0);
}
