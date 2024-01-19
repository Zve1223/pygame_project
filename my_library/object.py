from __future__ import annotations
import levels
import my_library
from my_library.component import Component
from my_library.transform import Transform


class Object:
    name: str
    transform: Transform
    components: list[Component]
    parent: Object | my_library.Hierarchy
    children: list[Object]

    def __init__(self, name: str = 'GameObject') -> None:
        self.name: str = name
        self.transform = Transform()
        self.components = []
        self.parent = levels.current_level.hierarchy.add_object(self)
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

    def add_component(self, component_type: type) -> None:
        if any(type(component) is component_type for component in self.components):
            print(f'Error! There is already {component_type} in components of {self.name}')
            return
        component = component_type(self)
        self.components.append(component)
        component.awake()
        component.start()

    def get_component(self, component_type: type) -> Component | None:
        for component in self.components:
            if type(component) is component_type:
                return component
        return None

    def find(self, object: Object) -> Object | None:
        for child in self.children:
            if child is object:
                return child
        for child in self.children:
            found = child.find(object)
            if found is not None:
                return found
        return None

    def delete(self) -> None:
        for component in self.components:
            component.delete()
        for child in self.children:
            child.delete()
