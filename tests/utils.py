from __future__ import annotations

import traceback
from typing import Any, TypeVar, cast
from typing_extensions import Literal, get_args, get_origin, assert_type

from modern_treasury._utils import is_dict, is_list, is_list_type, is_union_type
from modern_treasury._models import BaseModel

BaseModelT = TypeVar("BaseModelT", bound=BaseModel)


def assert_matches_model(model: type[BaseModelT], value: BaseModelT, *, path: list[str]) -> bool:
    for name, field in model.__fields__.items():
        field_value = getattr(value, name)

        if field.allow_none and field_value is None:
            continue

        assert_matches_type(field.outer_type_, field_value, path=[*path, name])

    return True


# Note: the `path` argument is only used to improve error messages when `--showlocals` is used
def assert_matches_type(type_: Any, value: object, *, path: list[str]) -> None:
    origin = get_origin(type_) or type_

    if is_list_type(type_):
        return _assert_list_type(type_, value)

    if origin == str:
        assert isinstance(value, str)
    elif origin == int:
        assert isinstance(value, int)
    elif origin == bool:
        assert isinstance(value, bool)
    elif origin == float:
        assert isinstance(value, float)
    elif origin == object:
        # nothing to do here, type expected type is unknown
        pass
    elif origin == Literal:
        assert value in get_args(type_)
    elif origin == dict:
        assert is_dict(value)

        args = get_args(type_)
        key_type = args[0]
        items_type = args[1]

        for key, item in value.items():
            assert_matches_type(key_type, key, path=[*path, "<dict key>"])
            assert_matches_type(items_type, item, path=[*path, "<dict item>"])
    elif is_union_type(type_):
        for i, variant in enumerate(get_args(type_)):
            try:
                assert_matches_type(variant, value, path=[*path, f"variant {i}"])
                return
            except AssertionError:
                traceback.print_exc()
                continue

        assert False, "Did not match any variants"
    elif issubclass(origin, BaseModel):
        assert isinstance(value, type_)
        assert assert_matches_model(type_, cast(Any, value), path=path)
    else:
        assert None, f"Unhandled field type: {type_}"


def _assert_list_type(type_: type[object], value: object) -> None:
    assert is_list(value)

    inner_type = get_args(type_)[0]
    for entry in value:
        assert_type(inner_type, entry)  # type: ignore
