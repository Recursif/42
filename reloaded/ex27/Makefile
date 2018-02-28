# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jdumorti <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/11/09 15:17:27 by jdumorti          #+#    #+#              #
#    Updated: 2017/11/10 16:24:37 by jdumorti         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = ft_display_file
FLAG = -Wall -Wextra -Werror
SRC = ft_display_file.c

OBJ = ft_display_file.o


all: $(NAME)

$(NAME):
	gcc $(FLAG) -o $(NAME) $(SRC)


clean:
	/bin/rm -f $(OBJ)
fclean: clean
	/bin/rm -f $(NAME)

re: fclean all
