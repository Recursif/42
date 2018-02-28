
#include <string.h>
#include "libft.h"

char	*ft_strncpy(char *dest, const char *src, size_t len)
{
	size_t	i;
	size_t	n;

	i = 0;
	n = ft_strlen(src);
	while (i < len)
	{
		if (i < n)
			dest[i] = src[i];
		else
			dest[i] = '\0';
		i++;
	}
	return (dest);
}
