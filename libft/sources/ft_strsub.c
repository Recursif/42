
#include <stdlib.h>

char	*ft_strsub(char const *s, unsigned int start, size_t len)
{
	char			*res;
	unsigned int	i;

	if (!s)
		return (NULL);
	res = (char *)malloc(sizeof(char) * (len + 1));
	if (!res)
		return (NULL);
	i = 0;
	while (len)
	{
		res[i] = s[i + start];
		len--;
		i++;
	}
	res[i] = '\0';
	return (res);
}
