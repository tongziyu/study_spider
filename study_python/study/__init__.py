# 在init,py文件中指定这个包被导入后，可以用的模块，如果没有写在__all__变量里，则不能用
# 这种只是针对 from ** import * 这种方式， 对于 import ** 则无用
__all__ = ["my_module1", "my_module2"]