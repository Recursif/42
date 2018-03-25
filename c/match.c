



int		ft_match(char *s1, char *s2, int r)
{
	if (*s1 == '\0' && (*s2 == '\0' || *s2 == '*'))
		return (1);
	if (*s1 == '\0' || *s2 == '\0')
		return (0);
	if (*s1 == *s2 && *s2 != '*')
		return ft_match(s1 + 1, s2 + 1);
	if ()

		
