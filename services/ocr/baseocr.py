from typing import Protocol, List

import numpy.typing as npt


# TODO change
class BASEOCR(Protocol):
    def extracted_tables_to_label_studio_json_file_with_paddleOCR(self, images_folder_path: str) -> str:
        ...

    def create_image_url(self, filename: str) -> str:
        ...

    def convert_bounding_box(self, bounding_box: list[float]):
        ...

    def create_image_url(self, filename: str) -> str:
        ...

    def convert_to_ls(self, image, tesseract_output, per_level='block_num'):
        ...


class BaseOCR:
    def detect_text(self, image: npt.NDArray) -> List[int, str]:
        raise NotImplementedError
