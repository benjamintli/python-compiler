from llvmlite import ir

class Number():
    def __init__(self, builder, module, value):
        self.builder = builder
        self.module = module
        self.value = value

    def eval(self):
        i = ir.Constant(ir.IntType(8), int(self.value))
        return i


class BinaryOp():
    def __init__(self, builder, module, left, right):
        self.builder = builder 
        self.module = module
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        ir_sum = self.builder.add(self.left.eval(), self.right.eval())     
        return ir_sum


class Sub(BinaryOp):
    def eval(self):
        ir_sub = self.builder.sub(self.left.eval(), self.right.eval())
        return ir_sub


class Div(BinaryOp):
    def eval(self):
        ir_div = self.builder.udiv(self.left.eval(), self.right.eval())
        return ir_div


class Mul(BinaryOp):
    def eval(self):
        ir_mul = self.builder.mul(self.left.eval(), self.right.eval())
        return ir_mul


class Mod(BinaryOp):
    def eval(self):
        ir_mod = self.builder.urem(self.left.eval(), self.right.eval())
        return ir_mod


class Or(BinaryOp):
    def eval(self):
        ir_or = self.builder.or_(self.left.eval(), self.right.eval())
        return ir_or


class And(BinaryOp):
    def eval(self):
        ir_and = self.builder.and_(self.left.eval(), self.right.eval())
        return ir_and


class Xor(BinaryOp):
    def eval(self):
        ir_xor = self.builder.xor(self.left.eval(), self.right.eval())
        return ir_xor


class Comparison(BinaryOp):
    def __init__(self, builder, module, left, right, comparison):
        super().__init__(builder, module, left, right)
        self.comparison = comparison

    def eval(self):
        ir_cmp = self.builder.icmp_unsigned(self.comparison, self.left.eval(), self.right.eval())
        return ir_cmp


class Print():
    def __init__(self, builder, module, printf, value):
        self.builder = builder
        self.module = module
        self.printf = printf
        self.value = value
    
    def eval(self):
        value = self.value.eval()

        # args list for print function
        voidptr_ty = ir.IntType(8).as_pointer()
        fmt = "%i \n\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)), 
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True
        global_fmt.initializer = c_fmt
        fmt_arg = self.builder.bitcast(global_fmt, voidptr_ty)
        
        # call function
        self.builder.call(self.printf, [fmt_arg, value])
