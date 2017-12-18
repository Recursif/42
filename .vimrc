set nocompatible
filetype off

set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

Plugin 'VundleVim/Vundle.vim'

" PLugin color
Plugin 'flazz/vim-colorschemes'
"Lib 9 utile pour certains plugins comme autocomplpop
Plugin 'eparreno/vim-l9'
"Autocomplete 
Plugin 'othree/vim-autocomplpop'
"Syntax Checker
Plugin 'scrooloose/syntastic'


" syntax hilight
Plugin 'octol/vim-cpp-enhanced-highlight'
Plugin 'luochen1990/rainbow'

" All of your Plugins must be added before the following line

call vundle#end()            " required
filetype plugin indent on    " required

" Visual settings
set t_Co=256                     " force vim to use 256 colors
set background=dark

" coloschemes

colorscheme kalahari
" diffrentes options
set number

" rainbow
let g:rainbow_active = 1

" Highlighting spaces and tabulations {{{
" (\zs & \ze == start and end of match, \s == any space)
match ErrorMsg '\s\+$'           " Match trailing whitespace
match ErrorMsg '\ \+\t'          " & spaces before a tab
match ErrorMsg '[^\t]\zs\t\+'    " & tabs not at the begining of a line
match ErrorMsg '\[^\s\]\zs\ \{2,\}' " & 2+ spaces not at the begining of a line
" }}}

if &t_Co > 2 || has("gui_running")
	syntax on
	set hlsearch
endif

if exists('+colorcolumn')
	set colorcolumn=80
endif

" status line
set laststatus=2                 " always display the status line
set shortmess=atI                " short messages to avoid scrolling
set title
set ruler                        " show the cursor position all the time
set showcmd                      " display incomplete commands


" autocompletion {{{
set wildmenu                     " show more than one suggestion for
" completion
set wildmode=list:longest        " shell-like completion (up to ambiguity
" point)
set wildignore=*.o,*.out,*.obj,*.pyc,.git,.hgignore,.svn,.cvsignore

set autoread                     " watch if the file is modified outside of
" vim
set hidden                       " allow switching edited buffers without
" saving
" }}}

" split screen below and right instead of vim natural
set splitbelow
set splitright
"
" desactivation des fleches
" Remplacer par espaces
":map <DOWN> :wincmd j<CR>
":map <UP> :wincmd k<CR>
":map <LEFT> :wincmd h<CR> 
":map <RIGHT> :wincmd l<CR>

":inoremap <DOWN> <Nop>
":inoremap <Up> <Nop>
":inoremap <LEFT> <Nop>
":inoremap <RIGHT> <Nop>

"raccourcis pour la creation et la navigation des onglets
noremap <C-T> :tabedit<space>
noremap <TAB> :tabnext <cr>
noremap <S-TAB> :tabprevious <cr>

"Configuration de syntastic
let g:syntastic_cpp_compiler = 'gcc'
let g:syntastic_cpp_compiler_options = ' -std=c++11 -stdlib=libc++ -Wall -Werror -Wextra'
let g:syntastic_check_on_open=1
let g:syntastic_enable_signs=1
let g:syntastic_cpp_check_header = 1
let g:syntastic_cpp_remove_include_errors = 1
let g:syntastic_c_remove_include_errors = 1
let g:syntastic_c_include_dirs = ['../../../includes', '../../includes','../includes','./includes', '../libft/includes', 'libft/includes']
