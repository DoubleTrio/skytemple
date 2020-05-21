#  Copyright 2020 Parakoopa
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
import os
from typing import Optional

from gi.repository.Gtk import TreeStore, TreeIter

from skytemple.core.abstract_module import AbstractModule
from skytemple.core.rom_project import RomProject
from skytemple.core.ui_utils import generate_item_store_row_label
from skytemple.module.rom.controller.main import MainController


class RomModule(AbstractModule):
    @classmethod
    def depends_on(cls):
        return []

    def __init__(self, rom_project: RomProject):
        """Main ROM metadata management module."""
        self.project = rom_project
        self._root_node: Optional[TreeIter] = None

    def get_root_node(self):
        return self._root_node

    def load_tree_items(self, item_store: TreeStore, root_node: TreeIter):
        self._root_node = item_store.append(root_node, [
            'folder-documents-symbolic', os.path.basename(self.project.filename), self,
            MainController, 0, False, ''
        ])
        generate_item_store_row_label(item_store[self._root_node])