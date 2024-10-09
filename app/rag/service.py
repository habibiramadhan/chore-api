from sqlalchemy import Table, Column, Integer, String, MetaData, inspect
from app.database import engine
from typing import List
from fastapi import UploadFile
from langchain.text_splitter import RecursiveCharacterTextSplitter
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

    def __chunk_pdf(self, pages:fitz.Document, char_limit:int = 1000, overlap:int = 100) -> List[str]:
        # Initialize
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=char_limit, chunk_overlap=overlap)
        chunks = []
        text = ""
        
        # Combine all text in pdf file
        for page in pages:
            text += (page.get_text().encode("ascii", "ignore").decode("utf-8", "ignore") + " ")

        # Split text into chunks
        chunks = text_splitter.split_text(text)

        return chunks

    def __add_chunk_to_table(self, chunks:List[str])->None:
        pass

    async def add_documents(self, username:str, file:UploadFile) -> None:
        table_name = f'documents_{username.replace(" ","")}'
        
        # Create new table if it doesn't exist
        if not inspect(engine).has_table(table_name):
            self.__create_user_documents_table(table_name)
        
        # Load file
        pages = await self.__load_pdf_file(file)

        # Chunking
        chunks = self.__chunk_pdf(pages)
        
        # # Add chunk to table
        # self.__add_chunk_to_table(chunks)