from typing import Callable, List, Optional

from libs.pip import InstallRequirement
from libs.pip import RequirementSet

InstallRequirementProvider = Callable[
    [str, Optional[InstallRequirement]], InstallRequirement
]


class BaseResolver:
    def resolve(
        self, root_reqs: List[InstallRequirement], check_supported_wheels: bool
    ) -> RequirementSet:
        raise NotImplementedError()

    def get_installation_order(
        self, req_set: RequirementSet
    ) -> List[InstallRequirement]:
        raise NotImplementedError()
