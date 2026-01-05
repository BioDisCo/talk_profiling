"""Demo for large memory usage and garbage collection callbacks."""

import gc

def cb(phase: str, info: dict) -> None:
    """GC callback to print phase and info."""
    print(phase, info)

gc.callbacks.append(cb)


class C:
    """Simple class with a pointer to another instance."""
    pointer: "C | None" = None


for i in range(10):
    # Our object container
    objs = []
    for _ in range(5_000_000):
        # Create a 3-cycle
        x = C()
        y = C()
        z = C()
        x.pointer = y
        y.pointer = z
        z.pointer = x

        # Add the first object in the cycle to the container
        objs.append(x)
    
    # Finally delete the container to make all objects unreachable
    # This will trigger garbage collection and may take significant time
    del objs
