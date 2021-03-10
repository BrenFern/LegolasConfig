"Plugins
call plug#begin()
Plug 'instant-markdown/vim-instant-markdown', {'for': 'markdown'}
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'jiangmiao/auto-pairs'
Plug 'terryma/vim-multiple-cursors'
Plug 'sheerun/vim-polyglot'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'preservim/nerdtree'
Plug 'jistr/vim-nerdtree-tabs'
Plug 'dense-analysis/ale'
Plug 'ayu-theme/ayu-vim'
Plug 'Yggdroot/indentLine'
Plug 'vim-python/python-syntax'
Plug 'ryanoasis/vim-devicons'
Plug 'python-mode/python-mode', { 'for': 'python', 'branch': 'develop' }
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'junegunn/vim-emoji'
Plug 'roxma/nvim-completion-manager'
call plug#end()

"ConfigurarMarkdowneemojiesinppets

"Autocmd
autocmd vimEnter * NERDTree
autocmd BufEnter * NERDTreeMirror

"ColorScheme
colorscheme ayu

"Syntax
syntax on 

"Lets
let ayucolor="dark" 
let g:ale_completion_enabled = 1
let g:indentLine_char = '|'
let g:indentLine_first_char = '|'
let g:indentLine_showFirstIndentLevel = 1
let g:deoplete#enable_at_startup = 1
let g:UltiSnipsEditSplit = 'vertical'
let g:UltiSnipsSnippetsDir = '~/config/nvim/UltiSnips'
let g:python_highlight_all = 1

"Sets
set hidden
set relativenumber
set inccommand=split
set termguicolors 

"Atalhos
let mapleader="\<space>"
nnoremap <leader>env :vsplit ~/.config/nvim/init.vim<cr>
nnoremap <leader>sv :source ~/.config/nvim/init.vim<cr>
nnoremap <leader>H :History<cr>
nnoremap <leader>A :Ag<space>
nnoremap <leader>F :Files<cr>
nnoremap<leader>B :Buffers<cr>

