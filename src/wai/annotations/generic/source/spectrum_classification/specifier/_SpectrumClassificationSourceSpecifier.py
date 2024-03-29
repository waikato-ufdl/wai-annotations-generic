from typing import Type, Tuple

from wai.annotations.core.component import Component
from wai.annotations.core.domain import DomainSpecifier
from wai.annotations.core.specifier import SourceStageSpecifier


class SpectrumClassificationSourceSpecifier(SourceStageSpecifier):
    """
    Specifies the generic spectrum classification source.
    """
    @classmethod
    def description(cls) -> str:
        return "Generic spectrum classification source."

    @classmethod
    def components(cls) -> Tuple[Type[Component], ...]:
        from wai.annotations.generic.source.base.component import BaseSource
        return BaseSource,

    @classmethod
    def domain(cls) -> Type[DomainSpecifier]:
        from wai.annotations.domain.spectra.classification import SpectrumClassificationDomainSpecifier
        return SpectrumClassificationDomainSpecifier
