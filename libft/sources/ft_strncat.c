
#include <string.h>
#include "libft.h"

char	*ft_strncat(char *dest, const char *src, size_t n)
{
	size_t	len;
	size_t	i;

	len = ft_strlen(dest);
	i = 0;
	while (i < n && src[i])
	{
		dest[len + i] = src[i];
		i++;
	}
	dest[i + len] = '\0';
	return (dest);
}
