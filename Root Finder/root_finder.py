from sympy import symbols, lambdify, init_printing, diff

init_printing();
x = symbols('x');

def input_function():
    expression = input("Enter the expression of the function in terms of 'x': ");
    
    try:
        function = lambdify(x, expression);
        return (function, expression);

    except Exception as e:
        print("Error when creating function:", e);
        return None

def bissection(f, a, b):
    valor = (a + b) / 2;
    print(f"a={a}, b={b}, x={valor}, f(x)={f(valor):.4f}");
    return valor;

def false_position(f, a, b):
    valor = (a * f(b) - b * f(a)) / (f(b) - f(a));
    print(f"a={a}, f(a)={f(a):.4f}, b={b}, f(b)={f(b):.4f}, x={valor:.4f}, f(x)={f(valor):.4f}");
    return valor;

def newton_raphson(f, expr, xn):
    der = diff(expr, x);
    der = lambdify(x, der);
    valor = xn - (f(xn) / der(xn));
    print(f"x={xn:.4f}, f(x)={f(xn):.4f}, f'(x)={der(xn):.4f}, xn={valor:.4f}, f(xn)={f(valor):.4f}");
    return valor;

def secant(f, a, b):
    valor = (a * f(b) - b * f(a)) / (f(b) - f(a));
    print(f"Xn-1={a}, f(Xn-1)={f(a):.4f}, Xn={b}, f(Xn)={f(b):.4f}, Xn+1={valor:.4f}, f(Xn+1)={f(valor):.4f}");
    return valor;

def get_root(method, function, a, b, e=1e-2):
    f = function[0];
    expr = function[1];
    iteration = 1;
    valor = None;
    while(1):
        if method == 4:
            valor = secant(f, a, b);
            a, b = b, valor;
        
        else:
            if method == 1:
                valor = bissection(f, a, b);
            
            elif method == 2:
                valor = false_position(f, a, b);
            
            else:
                valor = (a + b) / 2 if valor is None else valor;
                valor = newton_raphson(f, expr, valor);
            
            
            if f(a) * f(valor) > 0:
                a = valor;
            
            else:
                b = valor;
        
        
        if abs(f(valor)) < e:
            print(f"The root is {valor:.4f} in the iteration {iteration}");
            break;
        
        iteration += 1;
    

def main():
    f = input_function();
    method = int(input("Which method?:\n1 - Bissection\n2 - False Position\n3 - Newton-Raphson\n4 - Secant\n"));
    a = float(input("Type the value of a: "));
    b = float(input("Type the value of b: "));

    get_root(method, f, a, b);

main()
