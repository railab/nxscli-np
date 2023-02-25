"""Numpy based plugins list."""

from typing import TYPE_CHECKING

from nxscli.iplugin import DPluginDescription

from nxscli_np.commands.cmd_npmem import cmd_pnpmem
from nxscli_np.commands.cmd_npsave import cmd_pnpsave
from nxscli_np.plugins.npmem import PluginNpmem
from nxscli_np.plugins.npsave import PluginNpsave

if TYPE_CHECKING:
    import click

plugins_list: list[DPluginDescription] = [
    DPluginDescription("npsave", PluginNpsave, cmd_pnpsave),
    DPluginDescription("npmem", PluginNpmem, cmd_pnpmem),
]

configs_list: list["click.Command"] = []
