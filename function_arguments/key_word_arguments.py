"""keyword arguments => passing arguments with variable name.order is not an issue but no. of arguments does matter"""
"""keyword argument should come after positional argument""" #Positional arguments are arguments that are pass to function in proper positional order. 
def parents(dad,mom):
    print(f"dad: {dad}, mom: {mom}")

parents(dad="dulfacker", mom="jouhara") #kewyword arguments
parents("dulfacker", mom="jouhara")  #keyword argument should come after positional argument
