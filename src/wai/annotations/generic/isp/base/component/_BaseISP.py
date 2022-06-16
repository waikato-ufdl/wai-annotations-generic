from wai.common.cli.options import TypedOption
from wai.annotations.core.component import ProcessorComponent
from wai.annotations.core.stream import ThenFunction, DoneFunction
from wai.annotations.core.stream.util import RequiresNoFinalisation
from wai.annotations.domain.image import ImageInstance
from wai.annotations.generic.core import initialize_user_class


class BaseISP(
    RequiresNoFinalisation,
    ProcessorComponent[ImageInstance, ImageInstance]
):
    """
    Base class for generic stream processors.
    """

    user_class: str = TypedOption(
        "-c", "--class",
        type=str,
        help="the user class to wrap (dot notation)"
    )

    user_options: str = TypedOption(
        "-o", "--options",
        type=str,
        help="the options for the user class to parse"
    )

    def process_element(
            self,
            element: ImageInstance,
            then: ThenFunction[ImageInstance],
            done: DoneFunction
    ):
        if not hasattr(self, "_wrapped"):
            self._wrapped = initialize_user_class(self.user_class, self.user_options, ProcessorComponent)

        self._wrapped.process_element(element, then, done)
