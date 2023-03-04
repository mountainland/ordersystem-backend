# Expose a limited set of classes and functions so callers outside of
# the vcs package don't need to import deeper than `pip._internal.vcs`.
# (The test directory may still need to import from a vcs sub-package.)
# Import all vcs modules to register each VCS in the VcsSupport object.
from libs import pip
import libs.pip._internal.vcs.git
import libs.pip._internal.vcs.mercurial
import libs.pip._internal.vcs.subversion  # noqa: F401
from libs.pip import (  # noqa: F401
    RemoteNotFoundError,
    RemoteNotValidError,
    is_url,
    make_vcs_requirement_url,
    vcs,
)
