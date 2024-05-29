expr = input().replace("=", "==")
print("Yes") if eval(expr) else print(eval(expr.split("==")[0]))
