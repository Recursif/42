
#include <stdio.h>
#include <stdlib.h>

int   ft_difficulty(void)
{
  int   difficulty;

  difficulty = 0;
  while (difficulty < 1 || difficulty > 3)
  {
    printf("Choisir la difficulte:\n1 = entre 1 et 100\n\n2 = entre 1 et 1000\n\n3 = entre 1 et 10000\n");
    scanf("%d", &difficulty);
    printf("what\n");
  }

  if (difficulty == 1)
  {
    difficulty = 100;
    return (difficulty);
  }
  else if (difficulty == 2)
  {
    difficulty = 1000;
    return (difficulty);
  }
  else
  {
    difficulty = 10000;
    return (difficulty);
  }
}

int   ft_rand_a_b(int a, int b)
{
  return (rand() % (b - a) + 1);
}

int   main(void)
{
  int   number;
  int   counter;
  int   max_number;
  int   guess;
  int  continuerPartie;

  max_number = ft_difficulty();
  printf("%i\n", max_number);
  number = ft_rand_a_b(1, max_number);
  continuerPartie = 1;
  counter = 0;
  /* Boucle principal*/
  while (continuerPartie)
  {
    /*Choix*/
    printf("Choisir un nombre entre 1 et %i ou taper -1 pour quitter :\n", max_number);
    scanf("%d", &guess);
    /* Conditions*/
    if (guess == number)
    {
      printf("Felicitation vous avez gagnez!!\n");
      continuerPartie = 0;
      counter++;
    }
    else if (guess >= 1 && guess <= max_number)
    {
      if (guess < number)
        printf("Plus!!\n");
      else
        printf("Moins!!\n");
      counter++;
    }
    else if (guess == -1)
    {
      printf("Vous avez quitte la partie!!\n");
      continuerPartie = 0;
    }
    else
    {
      printf("Entree incorrect!!\n");
    }
  }
  printf("Vous avez joue %i coups\n", counter);
  return (0);
}
