"""Metadata generation logic for source distributions.
"""

import os

from libs.pip import Pep517HookCaller

from libs.pip import BuildEnvironment
from libs.pip import runner_with_spinner_message
from libs.pip import TempDirectory


def generate_editable_metadata(
    build_env: BuildEnvironment, backend: Pep517HookCaller
) -> str:
    """Generate metadata using mechanisms described in PEP 660.

    Returns the generated metadata directory.
    """
    metadata_tmpdir = TempDirectory(kind="modern-metadata", globally_managed=True)

    metadata_dir = metadata_tmpdir.path

    with build_env:
        # Note that Pep517HookCaller implements a fallback for
        # prepare_metadata_for_build_wheel/editable, so we don't have to
        # consider the possibility that this hook doesn't exist.
        runner = runner_with_spinner_message(
            "Preparing editable metadata (pyproject.toml)"
        )
        with backend.subprocess_runner(runner):
            distinfo_dir = backend.prepare_metadata_for_build_editable(metadata_dir)

    return os.path.join(metadata_dir, distinfo_dir)