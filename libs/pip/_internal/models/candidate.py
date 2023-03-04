from libs.pip import parse as parse_version

from libs.pip import Link
from libs.pip import KeyBasedCompareMixin


class InstallationCandidate(KeyBasedCompareMixin):
    """Represents a potential "candidate" for installation."""

    __slots__ = ["name", "version", "link"]

    def __init__(self, name: str, version: str, link: Link) -> None:
        self.name = name
        self.version = parse_version(version)
        self.link = link

        super().__init__(
            key=(self.name, self.version, self.link),
            defining_class=InstallationCandidate,
        )

    def __repr__(self) -> str:
        return "<InstallationCandidate({!r}, {!r}, {!r})>".format(
            self.name,
            self.version,
            self.link,
        )

    def __str__(self) -> str:
        return "{!r} candidate (version {} at {})".format(
            self.name,
            self.version,
            self.link,
        )
