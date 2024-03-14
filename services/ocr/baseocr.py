from typing import List
from abc import ABC, abstractmethod
import numpy.typing as npt

class BaseOCR(ABC):
    @abstractmethod
    def create_image_url(self,filename: str)-> str:
        raise NotImplementedError
    
    @abstractmethod
    def extracted_tables_to_label_studio_json_file(self, images_folder_path: str) -> None:
        raise NotImplementedError