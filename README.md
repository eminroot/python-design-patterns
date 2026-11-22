# Python Design Patterns

Small, readable implementations of classic Gang of Four design patterns in Python, each with a before/after example showing which SOLID principle the pattern protects.

## Creational

| Pattern | What it shows |
|---|---|
| [`shape`](shape/) | Shape area and perimeter without a pattern: the baseline that the factory version refactors. |
| [`factory`](factory/) | Factory Method: create shapes through a factory so new shapes are added without touching existing code (open/closed principle). |
| [`builder`](builder/) | Builder: assemble a House step by step through a HouseBuilder instead of a long constructor. |
| [`singleton`](singleton/) | Singleton: a Config class that always returns the same instance via __new__. |

## Structural

| Pattern | What it shows |
|---|---|
| [`facade`](facade/) | Facade: one start() call that drives TV, speaker and light subsystems behind a single interface. |

## Combined

| Pattern | What it shows |
|---|---|
| [`facadebuildersingleton`](facadebuildersingleton/) | Builder, Facade and Singleton combined in one small home-automation example. |

## Use

```bash
git clone https://github.com/eminroot/python-design-patterns
python3 python-design-patterns/<pattern>/<file>.py
```

## License

MIT
