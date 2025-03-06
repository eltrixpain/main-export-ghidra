# only change the output_path if you want

from ghidra.app.decompiler import DecompInterface
import sys

def find_function():
    """Find the specified function by name."""
    function_manager = currentProgram.getFunctionManager()
    
    for func in function_manager.getFunctions(True):
        if func.getName() == "main":
            return func
    return None

def export_function(func, output_file):
    """Export function details and decompiled code."""
    if not func:
        print("Function not found.")
        return
    
    with open(output_file, "w") as f:
        f.write("Function: {}\n".format(func.getName()))
        f.write("Address: {}\n".format(func.getEntryPoint()))
        
        decomp_interface = DecompInterface()
        decomp_interface.openProgram(currentProgram)
        results = decomp_interface.decompileFunction(func, 60, monitor)
        if results and results.decompileCompleted():
            f.write("\nDecompiled Code:\n")
            f.write(results.getDecompiledFunction().getC())
        else:
            f.write("\nFailed to decompile the function.")

args = getScriptArgs()
file = args[0] 
output_path = "/tmp/hamid/{}_export.txt".format(file)

target_func = find_function()
export_function(target_func, output_path)

print("Function '{}' exported to: {}".format(file, output_path))

