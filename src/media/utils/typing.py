from typing import Union, Any


AudioGeneratorInput = Union[str]
def is_audio_generator_input(value: Any) -> bool:
    return isinstance(value, str) # change the str to (str, float) or other type to add types


