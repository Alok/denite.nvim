# =============================================================================
# FILE: denite.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# =============================================================================

import neovim
from denite.denite import Denite


@neovim.plugin
class DeniteHandlers(object):
    def __init__(self, vim):
        self.__vim = vim

    @neovim.function('_denite', sync=True)
    def init_python(self, args):
        self.__denite = Denite(self.__vim)
        self.__vim.vars['denite#_channel_id'] = self.__vim.channel_id
        pass

    @neovim.command('Denite', sync=True, nargs='*')
    def start(self, args):
        self.__denite = Denite(self.__vim)
        self.__vim.vars['denite#_channel_id'] = self.__vim.channel_id
        self.__vim.vars['denite#args'] = args
        self.__denite.start({})
