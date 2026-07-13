from pathlib import Path
from gui.toast import Toast

import fitz          # PyMuPDF
from docx import Document


class FileLoader:
    """
    Utility class for loading supported text documents.

    Supported formats:
        - .txt
        - .pdf
        - .docx
    """

    SUPPORTED_EXTENSIONS = {
        ".txt",
        ".pdf",
        ".docx"
    }

    @classmethod
    def load(cls, file_path: str) -> str:
        """
        Load text from a supported file.

        Parameters
        ----------
        file_path : str
            Path to the file.

        Returns
        -------
        str
            Extracted text.

        Raises
        ------
        ValueError
            Unsupported file type.

        FileNotFoundError
            File does not exist.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(file_path)

        extension = path.suffix.lower()

        if extension not in cls.SUPPORTED_EXTENSIONS:
            raise ValueError(
                f"Unsupported file type: {extension}"
            )
            Toast(
                self,
                "Unsupported file format.",
                "error"
            )

        if extension == ".txt":
            return cls._load_txt(path)

        if extension == ".pdf":
            return cls._load_pdf(path)

        if extension == ".docx":
            return cls._load_docx(path)

        raise ValueError("Unknown file type.")

    # =====================================================
    # Private Loaders
    # =====================================================

    @staticmethod
    def _load_txt(path: Path) -> str:

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    @staticmethod
    def _load_pdf(path: Path) -> str:

        document = fitz.open(path)

        text = []

        for page in document:
            text.append(page.get_text())

        document.close()

        return "\n".join(text)

    @staticmethod
    def _load_docx(path: Path) -> str:

        document = Document(path)

        paragraphs = [
            paragraph.text
            for paragraph in document.paragraphs
        ]

        return "\n".join(paragraphs)