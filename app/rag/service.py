from sqlalchemy import Table, Column, Integer, String, MetaData, inspect
from app.database import engine
from typing import List
from fastapi import UploadFile
import fitz

class RAGService:
    # Create
    def __create_user_documents_table(self, table_name)->None:
        # Setup
        metadata = MetaData()
        user_documents_table = Table(
            table_name, metadata,
            Column("id", Integer, autoincrement=True, primary_key=True),
            Column("text", String),
        )

        # Create table to db
        metadata.create_all(engine)
    
    async def __load_pdf_file(self, file:UploadFile):
        contents = await file.read()
        pages = fitz.open(stream=contents, filetype="pdf")
        return pages

    def __chunk_text(self, texts:str) -> List[str]:
        pass

    def __add_chunk_to_table(self, chunks:List[str])->None:
        pass

    async def add_documents(self, username:str, file:UploadFile) -> None:
        table_name = f'documents_{username.replace(" ","")}'
        
        # Create new table if it doesn't exist
        if not inspect(engine).has_table(table_name):
            self.__create_user_documents_table(table_name)
        
        # Load file
        pages = await self.__load_pdf_file(file)

        # # Chunking
        # chunks = []
        # for page in pages:
        #     chunks += self.__chunk_text(page.get_text())
        
        # # Add chunk to table
        # self.__add_chunk_to_table(chunks)