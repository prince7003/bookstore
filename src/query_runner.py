import pandas as pd
import io
import sys
from groq_client import ask_groq

def run_query(user_query):
    # load data
    df_a = pd.read_csv("data/bookstore_a.csv")
    df_b = pd.read_csv("data/bookstore_b.csv")

    # load system prompt
    with open("prompts/system_prompt.txt") as f:
        system_prompt = f.read()

    # get pandas code from Groq
    code = ask_groq(system_prompt, user_query)
    print("🔹 Generated Code:\n", code)

    # execute safely
    local_vars = {"pd": pd, "df_a": df_a, "df_b": df_b}
    old_stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        exec(code, {}, local_vars)
        output = sys.stdout.getvalue().strip()
    finally:
        sys.stdout = old_stdout

    # If code defined a variable result, capture it
    result = local_vars.get("result", None)
    if result is not None:
        print("Query Output:\n", result)
        return result
    elif output:
        print("Query Output:\n", output)
        return output
    else:
        return None

if __name__ == "__main__":
    user_query = "Which bookstore sells the cheapest book overall?"
    # user_query = "Which is the top 5 highest rated Sci-Fi books across both bookstores?"
    run_query(user_query)
