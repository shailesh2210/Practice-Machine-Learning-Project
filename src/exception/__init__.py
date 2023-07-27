import os, sys

class CustomException(Exception):
    def __init__(self, error_message , error_detail):
        self.error_message = CustomException.get_error_detail_message(
            error_message=error_message , error_detail=error_detail)
        pass


    @staticmethod
    def get_error_detail_message(error_message: Exception , error_detail:sys)->str:
        _,_, exce_tb = error_detail.exc_info()
        exception_block_lineno = exce_tb.tb_frame.f_lineno
        try_block_lineno = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename

        error_message = f"""Error occur in script name [{file_name}]
        at try block line number [{try_block_lineno}]
        Exception Block line number[{exception_block_lineno}] 
        and error message [{error_message}]"""

        return error_message
    
    def __str(self):
        return self.error_message
    
    def __repr__(self):
        return CustomException.__name__.str()

