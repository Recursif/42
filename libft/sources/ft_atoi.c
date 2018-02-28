
int	ft_atoi(const char *str)
{
	int	res;
	int	neg;

	res = 0;
	neg = 1;
	while ((*str > 8 && *str < 14) || *str == ' ')
		str++;
	neg = (*str == '-') ? -1 : 1;
	str = (neg == -1 || *str == '+') ? str + 1 : str;
	while (*str >= '0' && *str <= '9')
		res = res * 10 + (*str++ - '0');
	return (res * neg);
}
