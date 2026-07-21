from app.rag.rag_pipeline import RAGPipeline

rag = RAGPipeline()

answer = rag.ask(

    "What is Secure Multi Party Computation?"

)

print()

print("="*60)

print(answer)