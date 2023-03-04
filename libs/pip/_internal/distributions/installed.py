from libs.pip import AbstractDistribution
from libs.pip import PackageFinder
from libs.pip import BaseDistribution


class InstalledDistribution(AbstractDistribution):
    """Represents an installed package.

    This does not need any preparation as the required information has already
    been computed.
    """

    def get_metadata_distribution(self) -> BaseDistribution:
        from libs.pip import Distribution as _Dist

        assert self.req.satisfied_by is not None, "not actually installed"
        return _Dist(self.req.satisfied_by)

    def prepare_distribution_metadata(
        self, finder: PackageFinder, build_isolation: bool
    ) -> None:
        pass
