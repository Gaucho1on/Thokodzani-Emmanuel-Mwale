1. PSEUDOCODE
Fibonacci  

START
INPUT n
SET a = 0
SET b = 1

FOR i = 1 TO n DO
    PRINT a
    SET temp = a + b
    SET a = b
    SET b = temp
END FOR

END
Factorial

START
INPUT n
SET fact = 1

FOR i = 1 TO n DO
    fact = fact * i
END FOR

PRINT fact
END

2. FLOW DIAGRAMS 
Fibonacci Flowchart

START
  |
INPUT n
  |
a = 0, b = 1
  |
i = 1
  |
[ i <= n ? ] ----No----> END
  |
 Yes
  |
PRINT a
  |
temp = a + b
a = b
b = temp
  |
i = i + 1
  |

Factorial Flowchart

START
  |
INPUT n
  |
fact = 1
i = 1
  |
[ i <= n ? ] ----No----> PRINT fact → END
  |
 Yes
  |
fact = fact * i
  |
i = i + 1
  |

3. CODE 

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return factorial