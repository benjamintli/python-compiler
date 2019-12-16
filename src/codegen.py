from llvmlite import ir, binding


class CodeGen():
    def __init__(self):
        self.binding = binding
        self.binding.initialize()
        self.binding.initialize_native_target()
        self.binding.initialize_native_asmprinter()
        self._config_llvm()
        self._create_execution_engine()
        self._declare_print_function()

    def create_ir(self):
        self._compile_ir()
    
    def save_ir(self, filename):
        with open(filename, 'w') as output_file:
            output_file.write(str(self.module))
    
    def _config_llvm(self):
        """
        configures LLVM
        """
        self.module = ir.Module(name=__file__)
        self.module.triple = self.binding.get_default_triple()
        func_type = ir.FunctionType(ir.VoidType(), [], False)
        base_func = ir.Function(self.module, func_type, name="main")
        block = base_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)
    
    def _create_execution_engine(self):
        """
        Create an execution engine that can do JIT code gen on
        the host CPU
        """
        target = self.binding.Target.from_default_triple()
        target_machine = target.create_target_machine()
        backing_module = binding.parse_assembly("")
        engine = binding.create_mcjit_compiler(backing_module, target_machine)
        self.engine = engine

    def _declare_print_function(self):
        """
        LLVM has no print function so we have to implement it
        """
        voidptr_ty = ir.IntType(8).as_pointer()
        printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)
        printf = ir.Function(self.module, printf_ty, name="printf")
        self.printf = printf

    def _compile_ir(self):
        """
        compile LLVM IR string to engine
        returns the module object
        """
        # create LLVM object
        self.builder.ret_void()
        llvm_ir = str(self.module)
        mod = self.binding.parse_assembly(llvm_ir)
        mod.verify()

        # add the module to the engine and compile it 
        self.engine.add_module(mod)
        self.engine.finalize_object()
        self.engine.run_static_constructors()
        return mod


