from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

def generar_resumen(contenido, config):
    """Generar un resumen del contenido con OpenAI"""
    try:
        llm = ChatOpenAI(
            model_name=config["model_name"],
            temperature=config["temperature"],
            openai_api_key=config["openai_api_key"]
        )
        
        prompt = (
            f"Por favor, genera un resumen conciso (150-200 palabras) del siguiente contenido, "
            f"manteniendo los puntos clave:\n\n{contenido}"
        )
        
        # Usamos invoke para evitar la deprecación
        respuesta = llm.invoke([HumanMessage(content=prompt)])
        return respuesta.content
    except Exception as e:
        print(f"Error al generar resumen: {e}")
        return "No se pudo generar el resumen."
