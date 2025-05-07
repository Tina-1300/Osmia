import os 

class FileCheck:
    def __init__(self, path):
        self.path_file = path
    
    def octet_to_mo(self, octet_size):
        return octet_size / (1024 * 1024)
    
    def file_exist(self, file_path) -> bool:
        return os.path.isfile(file_path)

    def size_files_limites(self, file_lst, email_service):
        if not isinstance(file_lst, list):
            raise TypeError("file_lst must be a list.")
        
        total_mo = 0.0
        for file in file_lst:
            if not os.path.isfile(file):
                raise FileNotFoundError(f"The file {self.path_file} does not exist.")
            
            byte_file = self.octet_to_mo(os.path.getsize(file))
            total_mo += byte_file

        if total_mo > email_service.size_max_file / (1024 * 1024): 
            raise ValueError(f"The total file size exceeds the allowed limit ({email_service.size_max_file / (1024 * 1024)} Mo)")
                