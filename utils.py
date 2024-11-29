import matplotlib.pyplot as plt_u
import numpy as np_u
import numpy.random as np_u_rand


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
        if verbose:
            print("El límite inferior es la raíz")
        return a

    if func(b) == 0:
        if verbose:
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
    El método de secante requiere dos aproximaciones iniciales de la raíz
    distintas que no necesariamente tienen que estar cerca de la raíz real.

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

    dx = (b - a) / n
    suma_lados = 0

    for i in range(n):
        if tipo == 'left':
            x_ev = a + i * dx

        elif tipo == 'right':
            x_ev = a + (i + 1) * dx

        else:  # center
            x_ev = a + (i + 1/2) * dx

        suma_lados += func(x_ev)

    suma_areas = suma_lados * dx

    return suma_areas


def grafico_barras(lanzamientos, porcentaje=False):
    """
    Función que grafica un histograma de los resultados de una
    serie de lanzamientos.

    Inputs:
    =======
    lanzamientos: lista de resultados de los lanzamientos
    porcentaje: si es True, se grafica el porcentaje de cada resultado

    Output:
    =======
    Gráfico de barras con los resultados de los lanzamientos
    """
    n = len(lanzamientos)

    counts = np_u.unique(lanzamientos, return_counts=True)
    etiquetas = counts[0]
    valores = counts[1] / n * 100 if porcentaje else counts[1]

    plt_u.bar(etiquetas, valores, edgecolor='black')
    plt_u.xlabel('Resultado')
    plt_u.ylabel('Frecuencia (%)' if porcentaje else 'Frecuencia')
    plt_u.grid(ls=':')

    plt_u.show()


def circ_en_cuadro(r, cuarto=True):
    """
    Función que grafica una circunferencia de radio r en un cuadrado
    de lado r

    Inputs:
    =======
    r: float
        radio de la circunferencia

    cuarto: bool, opcional
        si es True, se grafica solo un cuarto de la circunferencia
        si es False, se grafica la mitad de la circunferencia inscrito
        en un rectángulo de lado 2r y altura r

    Output:
    =======
    fig, ax: figuras de matplotlib

    Ejemplo:
    ========
    >>> fig, ax = circ_en_cuadro(1)
    """
    x_inicio = 0 if cuarto else -r

    fig, ax = plt_u.subplots(figsize=(5, 5),
                             subplot_kw={'aspect': 'equal'})
    zorder = 10
    # cuadrado
    ax.hlines([0, r], xmin=x_inicio, xmax=r,
              color="black", zorder=zorder)
    ax.vlines([x_inicio, r], ymin=0, ymax=r,
              color="black", zorder=zorder)

    # circunferencia
    x = np_u.linspace(x_inicio, r, 250)
    y = np_u.sqrt(r**2 - x**2)
    ax.plot(x, y, color='black', zorder=zorder)

    return fig, ax


# Evaluación final

def lago_simulador(radio=20, num_points=10_000, seed=42):
    """
    Función que simula un lago con una forma realista.

    Inputs:
    =======

    radio: float, opcional
        radio del lago

    num_points: int, opcional
        número de puntos a simular

    seed: int, opcional
        semilla para reproducibilidad

    Output:
    =======
    x_realista, y_realista: coordenadas de los puntos del lago

    [radio, amplitudes, frecuencias]: parámetros de la forma realista
    """

    np_u_rand.seed(seed)

    theta = np_u.linspace(0, 2 * np_u.pi, num_points)
    amplitudes = [np_u_rand.uniform(radio * 0.05, radio * 0.15),
                  np_u_rand.uniform(radio * 0.02, radio * 0.1),
                  np_u_rand.uniform(radio * 0.01, radio * 0.05)]

    frecuencias = [np_u_rand.uniform(1, 5),
                   np_u_rand.uniform(5, 10),
                   np_u_rand.uniform(10, 25)]

    radio_realista = np_u.sum([amplitudes[i] * np_u.sin(frecuencias[i] * theta)
                               for i in range(3)], axis=0)

    radio_realista += radio

    x_lago = radio_realista * np_u.cos(theta)
    y_lago = radio_realista * np_u.sin(theta)

    return x_lago, y_lago, [radio, amplitudes, frecuencias]


def plot_rectangulo(x_min, x_max, y_min, y_max):
    """
    Función que grafica un rectángulo en un plano cartesiano.

    Inputs:
    =======
    x_min, x_max: float
        límites en el eje x
    y_min, y_max: float
        límites en el eje y

    Output:
    =======
    Gráfico con el rectángulo dibujado
    """

    plt_u.hlines([y_min, y_max], xmin=x_min, xmax=x_max, color='black',
                 ls='--', lw=1)
    plt_u.vlines([x_min, x_max], ymin=y_min, ymax=y_max, color='black',
                 ls='--', lw=1)

    pass


def dentro_del_lago(x, y, datos_lago):
    """
    Función que verifica si un punto (x, y) está dentro del lago.

    Inputs:
    =======
    x: float
        coordenada x del punto

    y: float
        coordenada y del punto

    datos_lago: lista
        parámetros del lago generado con lago_simulador

    Output:
    =======
    bool: True si el punto está dentro del lago, False caso contrario
    """
    distancia = np_u.sqrt(x**2 + y**2)

    theta = np_u.arctan2(y, x)

    if theta < 0:
        theta += 2 * np_u.pi

    radio, amplitudes, frecuencias = datos_lago

    radio_lago = np_u.sum([amplitudes[i] * np_u.sin(frecuencias[i] * theta)
                           for i in range(3)], axis=0)

    radio_lago += radio

    if distancia <= radio_lago:
        return True

    return False


def plot_circunferencia(x_centro, y_centro, r, color=None):
    """
    Función que grafica una circunferencia en un plano cartesiano.

    Inputs:
    =======
    x_centro, y_centro: float
        coordenadas del centro de la circunferencia

    r: float
        radio de la circunferencia

    color: str, opcional
        color de la circunferencia

    Output:
    =======
    Gráfico con la circunferencia dibujada
    """

    theta = np_u.linspace(0, 2 * np_u.pi, 1_000)
    x = x_centro + r * np_u.cos(theta)
    y = y_centro + r * np_u.sin(theta)

    plt_u.plot(x, y, color=color)

    pass


def exponencial_taylor(x, n):
    """
    Función que calcula la aproximación de la función exponencial
    mediante la serie de Taylor.

    Inputs:
    =======
    x: float
        valor en el que se evalúa la función

    n: int
        número de términos de la serie de Taylor

    Output:
    =======
    float: aproximación de la función exponencial en x
    """

    return np_u.sum([x**i / np_u.math.factorial(i) for i in range(n)])
