def biseccion(func, a, b, tol=1e-8, max_iter=1_000, verbose=False):
    """
    Calcula la raíz de una función utilizando el método de bisección.

    Inputs:
    ----------
    func: function
        Función para la cual se desea encontrar la raíz.

    a: float
        Límite inferior del intervalo.

    b: float
        Límite superior del intervalo.

    tol: float, opcional
        Tolerancia para la convergencia (por defecto es 1e-8).

    max_iter: int, opcional
        Número máximo de iteraciones (por defecto es 1.000).

    verbose: bool, opcional
        Si es True, imprime el número de iteraciones y la raíz
        (por defecto es False).

    Output:
    --------
    float
        La raíz de la función dentro del intervalo dado, si se encuentra.
        Si no hay cambio de signo en los extremos del intervalo, retorna None.

    Notas:
    -----
    El método de bisección requiere que la función cambie de signo en los
    extremos del intervalo [a, b]. Esto significa que func(a) * func(b) < 0.

    Ejemplos:
    --------
    >>> def f(x):
    ...     return x**2 - 1
    >>> biseccion(f, 0, 2)
    1.0
    >>> biseccion(f, -2, 0)
    -1.0
    """

    if func(a) * func(b) > 0:
        print("No hay cambio de signo en los extremos del intervalo")
        return None

    if func(a) == 0:
        print("El límite inferior es la raíz")
        return a

    if func(b) == 0:
        print("El límite superior es la raíz")
        return b

    x_centro = (a + b) / 2
    n_iter = 0

    while (abs(b-a)/2 > tol) and (n_iter < max_iter):
        if func(x_centro) == 0:  # caso poco probable numéricamente
            if verbose:
                print(f"Se encontró la raíz exacta")
            break

        elif func(a) * func(x_centro) < 0:
            b = x_centro

        else:
            a = x_centro

        x_centro = (a + b) / 2
        n_iter += 1

    if n_iter == max_iter:
        print("No se encontró la raíz,",
              f"se alcanzó el número máximo de iteraciones {max_iter}")
        return None

    if verbose:
        print(f"La raíz encontrada en {n_iter} iteraciones es {x_centro}")

    return x_centro


def secante(func, x0, x1, tol=1e-8, max_iter=1_000, verbose=False):
    """
    Calcula la raíz de una función utilizando el método de la secante.

    Inputs:
    ----------
    func: function
        Función para la cual se desea encontrar la raíz.

    x0: float
        Primera aproximación inicial de la raíz.

    x1: float
        Segunda aproximación inicial de la raíz.

    tol: float, opcional
        Tolerancia para la convergencia (por defecto es 1e-8).

    max_iter: int, opcional
        Número máximo de iteraciones (por defecto es 1.000).

    verbose: bool, opcional
        Si es True, imprime el número de iteraciones y la raíz
        (por defecto es False).

    Output:
    --------
    float
        La raíz de la función dentro del intervalo dado, si se encuentra.
        Si no se encuentra la raíz, se imprime un mensaje de error y se
        retorna None.

    Notas:
    -----
    El método de secante requiere dos aproximaciones iniciales de la raíz distintas 
    que no necesariamente tienen que estar cerca de la raíz real.

    Ejemplos:
    --------
    >>> def f(x):
    ...     return x**2 - 4
    >>> secante(f, 0, 5)
    2.0
    >>> secante(f, -5, 0)
    -2.0
    """
    n_iter = 0

    if x1 == x0:
        print("Error: x0 y x1 son iguales")
        return None

    while (abs(x1 - x0) > tol) and (n_iter < max_iter):
        denominador = func(x1) - func(x0)

        if denominador == 0:  # Evitar división por cero
            print("Error: denominador igual a cero")
            return None

        x2 = x1 - func(x1) * (x1 - x0) / denominador
        x0, x1 = x1, x2
        n_iter += 1

    if n_iter == max_iter:
        print("No se encontró la raíz,",
              f"se alcanzó el número máximo de iteraciones {max_iter}")
        return None

    if verbose:
        print(f"La raíz encontrada en {n_iter} iteraciones es {x2}")

    return x2


def riemann_sum(func, a, b, n, tipo='right'):
    """
    Función que calcula la suma de Riemann de una función en
    un cierto intervalo [a, b] con n subintervalos.
    
    inputs:
    =======
    func: función a obtener el área bajo la curva
    a, b: límites del intervalo
    n: número de subintervalos
    tipo: tipo de suma de Riemann a calcular (right, left, center)
    
    output:
    =======
    suma_areas: suma de Riemann de la función en el intervalo [a, b]
    
    Ejemplo:
    ========
    >>> f = lambda x: x**2
    >>> riemann_sum(f, 0, 1, 1000, 'right')
    0.33383350000000034
    """

    if not (tipo in ['left', 'right', 'center']):
        print("los tipos admitidos son: left, right y center")
        return None
    
    suma_areas = 0
    dx = (b - a) / n
    
    for i in range(n):
        if tipo == 'left':
            x_ev = a + i * dx
        
        elif tipo == 'right':
            x_ev = a + (i + 1) * dx
        
        else:  # center
            x_ev = a + (i + 1/2) * dx
            
        suma_areas += dx * func(x_ev)
    
    return suma_areas