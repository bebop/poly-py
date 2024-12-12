# poly-py

python bindings for [Poly](https://github.com/bebop/poly), a Go package for engineering DNA.

These bindings are experimental and generated directly from poly's Go implementation.
They are here entirely for audit purposes. Any feature related issues or development should be made
in the [issues section of poly's main repo](https://github.com/bebop/poly/issues).

`pip install clonai`

`poetry add clonai`

```python

from poly import checks

isDNA? = checks.IsDNA("ACTC")

print(isDNA?)
```

If there's enough interest I'll

1. Refactor poly to make all or most features fully exportable to python
2. Solidify build pipeline so that other folk can easily write a deploy go packages to extend python
3. Release statically generated doc site for python bindings via readthedocs
4. Beg the current holder of the `poly` namespace on pypi to let this project use it so we can use, `pip install poly`
