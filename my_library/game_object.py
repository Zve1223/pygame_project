from __future__ import annotations
from typing import TypeVar, Type

from .component import Component
from .components.transform import Transform
from .hierarchy import Hierarchy
from . import hierarchy


_T = TypeVar('_T', bound=Component)


class GameObject:
    name: str
    transform: Transform
    components: list[Transform, Component, ...]
    parent: GameObject | Hierarchy
    children: list[GameObject, ...]

    def __init__(self, name: str = 'GameObject') -> None:
        self.name: str = name
        self.transform = Transform(self)
        self.components = [self.transform]
        self.parent = hierarchy.add_object(self)
        self.children = []

        self.awake()

    def __str__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.transform}, [{", ".join(map(str, self.components))}], ' \
               f'{self.parent.name}, {len(self.children)})'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.name}, {self.transform}, [{", ".join(map(str, self.components))}], ' \
               f'{self.parent.name}, {len(self.children)})'

    def awake(self) -> None:
        for component in self.components:
            component.awake()
        for child in self.children:
            child.awake()

    def start(self) -> None:
        for component in self.components:
            component.start()
        for child in self.children:
            child.start()

    def fixed_update(self) -> None:
        for component in self.components:
            component.fixed_update()
        for child in self.children:
            child.fixed_update()

    def update(self) -> None:
        for component in self.components:
            component.update()
        for child in self.children:
            child.update()

    def late_update(self) -> None:
        for component in self.components:
            component.late_update()
        for child in self.children:
            child.late_update()

    def add_component(self, component_type: Type[_T]) -> _T:
        for component in self.components:
            if type(component) is component_type:
                print(f'Error! There is already {component_type} in components of {self.name}')
                return component

        component = component_type(self)
        self.components.append(component)

        component.awake()
        component.start()

        return component

    def get_component(self, component_type: Type[_T]) -> _T | None:
        for component in self.components:
            if type(component) is component_type:
                return component
        return None

    def remove_component(self, component_type: Type[_T]) -> None:
        if component_type is Transform:
            print('Nope. You can\'t remove Transform component')
            return
        for component in self.components:
            if type(component) is component_type:
                self.components.remove(component)
                component.delete()
                return
        print(f'Error! There is no {component_type} in components of {self.name}')
        return None

    @classmethod
    def find_object(cls, name) -> GameObject | None:
        return hierarchy.find_object(name)

    def find(self, name: str) -> GameObject | None:
        for child in self.children:
            if child.name == name:
                return child
        for child in self.children:
            found = child.find(name)
            if found is not None:
                return found
        return None

    def delete(self) -> None:
        for component in self.components:
            component.delete()
        for child in self.children:
            child.delete()
