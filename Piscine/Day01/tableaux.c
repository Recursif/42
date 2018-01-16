#include <stdio.h>

int sommeTableau(int tableau[], int tailleTableau)
{
  int     sommeTab;
  int     cpt;

  cpt = 0;
  sommeTab = 0;
  while (tableau[cpt])
  {
    sommeTab += tableau[cpt];
    cpt++;
  }
  return (sommeTab);
}

double moyenneTableau(int tableau[], int tailleTableau)
{
  double  moyenneTab;

  moyenneTab = sommeTableau(tableau[], tailleTableau) / tailleTableau;
  return (moyenneTab);
}

void copie(int tableauOriginal[], int tableauCopie[], int tailleTableau)
{
  int     cpt;

  cpt = 0;
  while (tableauOriginal[cpt])
  {
    tableauCopie[cpt] = tableauOriginal[cpt];
  }
}

void maximumTableau(int tableau[], int tailleTableau, int valeurMax)
{
  int     cpt;

  cpt = 1;
  valeurMax = tableau[0];
  while (tableau[cpt])
  {
    if (valeurMax < tableau[cpt])
      valeurMax = tableau[cpt];
  }
}
void swap(int *a, int *b)
{
  int     x;

  x = *a;
  *a = *b;
  *b = x;
}



void ordonnerTableau(int tableau[], int tailleTableau);
{
  int     cpt;

  cpt = 1;
  while (tableau[cpt])
  {
    if (tableau[cpt - 1] > tableau[cpt])
      {
        swap(tableau[cpt - 1], tableau[cpt]);
        cpt = 1;
      }
    cpt++;
  }
}
