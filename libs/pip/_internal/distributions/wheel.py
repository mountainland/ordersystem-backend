from libs.pip import canonicalize_name

from libs.pip import AbstractDistribution
from libs.pip import PackageFinder
from libs.pip import (
    BaseDistribution,
    FilesystemWheel,
    get_wheel_distribution,
)


class WheelDistribution(AbstractDistribution):
    """Represents a wheel distribution.

    This does not need any preparation as wheels can be directly unpacked.
    """

    def get_metadata_distribution(self) -> BaseDistribution:
        """Loads the metadata from the wheel file into memory and returns a
        Distribution that uses it, not relying on the wheel file or
        requirement.
        """
        assert self.req.local_file_path, "Set as part of preparation during download"
        assert self.req.name, "Wheels are never unnamed"
        wheel = FilesystemWheel(self.req.local_file_path)
        return get_wheel_distribution(wheel, canonicalize_name(self.req.name))

    def prepare_distribution_metadata(
        self, finder: PackageFinder, build_isolation: bool
    ) -> None:
        pass