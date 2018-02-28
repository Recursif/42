
#include <string.h>

char	*ft_strchr(const char *s, int c)
{
	char	*str;

	str = (char *)s;
	while (*str && *str != (char)c)
		str++;
	return ((*str || (!*str && !c)) ? str : NULL);
}
