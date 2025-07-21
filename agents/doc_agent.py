from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from repo_utils.fetch_files import fetch_repo_files
from dotenv import load_dotenv
import os

load_dotenv()

def build_readme_chain(llm):
    prompt = PromptTemplate.from_file("prompts/readme_prompt.txt", input_variables=["repo_name", "file_list", "descriptions"])
    return LLMChain(llm=llm, prompt=prompt)

def extract_repo_name(repo_url):
    repo_name = repo_url.split("github.com/")[-1]
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]
    if "/" in repo_name:
        repo_name = repo_name.split("/")[-1]
    return repo_name

def generate_readme(repo_url):
    files = fetch_repo_files(repo_url)
    file_list = "\n".join([path for path, _ in files])
    descriptions = "\n\n".join([f"{path}:\n{content[:500]}" for path, content in files])
    repo_name = extract_repo_name(repo_url)

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7, google_api_key=os.getenv("GOOGLE_API_KEY"))
    chain = build_readme_chain(llm)
    return chain.run({"repo_name": repo_name, "file_list": file_list, "descriptions": descriptions})