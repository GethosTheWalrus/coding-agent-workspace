# app/crud/__init__.py
"""CRUD package exposing submodules for convenient imports.

The API layer accesses CRUD functions via ``crud.todo``. To make this work,
we import the ``todo`` submodule here so that it becomes an attribute of the
package.
"""

from . import todo  # noqa: F401  (re-export for ``app.crud.todo``)
