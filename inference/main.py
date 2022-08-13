from typing import List, Union
from fastapi import FastAPI
from pydantic import BaseModel
from deploy.predict import ArticleGenerator

app = FastAPI()

class ArticleRequest(BaseModel):
    content: str
    model_type: Union[str, None] = None

class ArticleResponse(BaseModel):
    title: str
    content: str
    summary: str
    keywords: List[str]

    
@app.post("/api/article/generate/", response_model = ArticleResponse) 
def root(article: ArticleRequest):
    articleGenerator = ArticleGenerator(article.content)
    title = articleGenerator.generate_title(article.model_type).replace(" ",'')
    summary = articleGenerator.generate_summary()
    keywords = articleGenerator.generate_keywords()
    return  ArticleResponse(title=title, 
                content=article.content,
                summary=summary,
                keywords=keywords)
